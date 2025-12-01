"""
Test per validare l'integrità dei dati dei comuni italiani.
Verifica che tutti i comuni abbiano i campi richiesti inclusi i dati sulla popolazione.
"""
import sys
from pathlib import Path

import pytest

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from lib import Loader
from models import Comune, ComuneBase


@pytest.fixture(scope="module")
def loader():
    """Crea un'istanza del loader per tutti i test."""
    return Loader()


@pytest.fixture(scope="module")
def all_comuni_mini(loader):
    """Carica il dataset ridotto di tutti i comuni."""
    return loader.load_mini()


@pytest.fixture(scope="module")
def all_comuni_full(loader):
    """Carica il dataset completo di tutti i comuni."""
    return loader.load_all()


class TestISTATCodes:
    """Test per la formattazione dei codici ISTAT."""

    def test_all_istat_codes_are_6_digits(self, all_comuni_full):
        """Verifica che tutti i codici ISTAT siano esattamente di 6 cifre."""
        invalid_codes = []
        for comune in all_comuni_full:
            pro_com_t = comune.get("pro_com_t", "")
            if len(pro_com_t) != 6:
                invalid_codes.append((comune.get("comune"), pro_com_t))

        assert not invalid_codes, (
            f"Trovati {len(invalid_codes)} comuni con codici ISTAT non validi: "
            f"{invalid_codes[:10]}"
        )

    def test_all_istat_codes_are_numeric(self, all_comuni_full):
        """Verifica che tutti i codici ISTAT contengano solo cifre."""
        non_numeric = []
        for comune in all_comuni_full:
            pro_com_t = comune.get("pro_com_t", "")
            if not pro_com_t.isdigit():
                non_numeric.append((comune.get("comune"), pro_com_t))

        assert not non_numeric, (
            f"Trovati {len(non_numeric)} comuni con codici ISTAT non numerici: "
            f"{non_numeric[:10]}"
        )


class TestPopulationData:
    """Test per l'integrità dei dati sulla popolazione."""

    def test_all_comuni_have_population_field(self, all_comuni_mini):
        """Verifica che tutti i comuni abbiano il campo pop_res_21."""
        missing_pop = []
        for comune in all_comuni_mini:
            if "pop_res_21" not in comune:
                missing_pop.append(
                    (comune.get("comune"), comune.get("pro_com_t"))
                )

        assert not missing_pop, (
            f"Trovati {len(missing_pop)} comuni senza il campo pop_res_21: "
            f"{missing_pop[:10]}"
        )

    def test_population_data_is_not_empty(self, all_comuni_mini):
        """Verifica che tutti i comuni abbiano dati sulla popolazione non vuoti."""
        empty_pop = []
        for comune in all_comuni_mini:
            pop = comune.get("pop_res_21")
            if not pop or pop.strip() == "":
                empty_pop.append(
                    (comune.get("comune"), comune.get("pro_com_t"))
                )

        assert not empty_pop, (
            f"Trovati {len(empty_pop)} comuni con dati sulla popolazione vuoti: "
            f"{empty_pop[:10]}"
        )

    def test_population_values_are_numeric(self, all_comuni_mini):
        """Verifica che i valori della popolazione siano stringhe numeriche."""
        non_numeric_pop = []
        for comune in all_comuni_mini:
            pop = comune.get("pop_res_21", "")
            if pop and not pop.isdigit():
                non_numeric_pop.append(
                    (comune.get("comune"), comune.get("pro_com_t"), pop)
                )

        assert not non_numeric_pop, (
            f"Trovati {len(non_numeric_pop)} comuni con popolazione non numerica: "
            f"{non_numeric_pop[:10]}"
        )

    def test_population_values_are_reasonable(self, all_comuni_mini):
        """Verifica che i valori della popolazione siano in un intervallo ragionevole (1-5.000.000)."""
        unreasonable_pop = []
        for comune in all_comuni_mini:
            pop = comune.get("pop_res_21", "")
            if pop and pop.isdigit():
                pop_int = int(pop)
                if pop_int < 1 or pop_int > 5_000_000:
                    unreasonable_pop.append(
                        (comune.get("comune"), comune.get("pro_com_t"), pop)
                    )

        assert not unreasonable_pop, (
            f"Trovati {len(unreasonable_pop)} comuni con popolazione non ragionevole: "
            f"{unreasonable_pop[:10]}"
        )


class TestRequiredFields:
    """Test per i campi obbligatori nei dati dei comuni."""

    def test_all_comuni_have_required_mini_fields(self, all_comuni_mini):
        """Verifica che tutti i comuni abbiano i campi richiesti per il modello ComuneBase."""
        required_fields = ["pro_com_t", "comune", "sigla"]
        missing_fields = []

        for comune in all_comuni_mini:
            for field in required_fields:
                if field not in comune or not comune[field]:
                    missing_fields.append(
                        (comune.get("comune"), comune.get("pro_com_t"), field)
                    )

        assert not missing_fields, (
            f"Trovati {len(missing_fields)} campi obbligatori mancanti: "
            f"{missing_fields[:10]}"
        )

    def test_comuni_mini_model_validation(self, all_comuni_mini):
        """Verifica che tutti i comuni possano essere validati con il modello ComuneBase."""
        invalid_comuni = []

        for comune_data in all_comuni_mini[:100]:  # Testa i primi 100 per velocità
            try:
                ComuneBase(**comune_data)
            except Exception as e:
                invalid_comuni.append(
                    (comune_data.get("comune"), comune_data.get("pro_com_t"), str(e))
                )

        assert not invalid_comuni, (
            f"Trovati {len(invalid_comuni)} comuni che non hanno superato la validazione del modello: "
            f"{invalid_comuni[:5]}"
        )

    def test_comuni_full_model_validation(self, all_comuni_full):
        """Verifica che tutti i comuni possano essere validati con il modello Comune."""
        invalid_comuni = []

        for comune_data in all_comuni_full[:100]:  # Testa i primi 100 per velocità
            try:
                Comune(**comune_data)
            except Exception as e:
                invalid_comuni.append(
                    (comune_data.get("comune"), comune_data.get("pro_com_t"), str(e))
                )

        assert not invalid_comuni, (
            f"Trovati {len(invalid_comuni)} comuni che non hanno superato la validazione completa del modello: "
            f"{invalid_comuni[:5]}"
        )


class TestDataConsistency:
    """Test per la coerenza dei dati tra i dataset."""

    def test_mini_and_full_datasets_have_same_comuni(self, all_comuni_mini, all_comuni_full):
        """Verifica che i dataset ridotto e completo abbiano gli stessi comuni."""
        mini_istats = {c.get("pro_com_t") for c in all_comuni_mini}
        full_istats = {c.get("pro_com_t") for c in all_comuni_full}

        only_in_mini = mini_istats - full_istats
        only_in_full = full_istats - mini_istats

        assert not only_in_mini, f"Trovati {len(only_in_mini)} comuni solo nel dataset ridotto"
        assert not only_in_full, f"Trovati {len(only_in_full)} comuni solo nel dataset completo"

    def test_population_percentage_coverage(self, all_comuni_mini):
        """Verifica che almeno il 95% dei comuni abbia dati sulla popolazione."""
        total = len(all_comuni_mini)
        with_population = sum(
            1 for c in all_comuni_mini
            if c.get("pop_res_21") and c.get("pop_res_21").strip()
        )

        coverage_percentage = (with_population / total) * 100

        assert coverage_percentage >= 95, (
            f"La copertura della popolazione è {coverage_percentage:.2f}%, attesa >= 95%. "
            f"{total - with_population} comuni mancano dei dati sulla popolazione."
        )


class TestDatasetStats:
    """Test per raccogliere statistiche sul dataset."""

    def test_print_dataset_statistics(self, all_comuni_mini, all_comuni_full):
        """Stampa statistiche utili sul dataset."""
        print(f"\n=== Statistiche Dataset ===")
        print(f"Totale comuni (ridotto): {len(all_comuni_mini)}")
        print(f"Totale comuni (completo): {len(all_comuni_full)}")

        with_pop = sum(
            1 for c in all_comuni_mini
            if c.get("pop_res_21") and c.get("pop_res_21").strip()
        )
        print(f"Comuni con dati sulla popolazione: {with_pop} ({with_pop/len(all_comuni_mini)*100:.2f}%)")

        # Ottieni statistiche sulla popolazione
        populations = [
            int(c.get("pop_res_21"))
            for c in all_comuni_mini
            if c.get("pop_res_21") and c.get("pop_res_21").isdigit()
        ]

        if populations:
            print(f"Popolazione minima: {min(populations)}")
            print(f"Popolazione massima: {max(populations)}")
            print(f"Popolazione media: {sum(populations) / len(populations):.0f}")
            print(f"Popolazione totale: {sum(populations):,}")
