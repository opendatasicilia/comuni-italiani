import csv
import json
from pathlib import Path


class Loader:
    def __init__(self):
        self.data_dir = self.get_data_dir()
        self.main_file = self.get_file_path("main.csv")
        self.pop_file = self.get_file_path("popolazione_2021.csv")
        self.map_file = self.get_file_path("geojson/comuni_siciliani2021_semplify.geojson")

    @staticmethod
    def get_data_dir():
        """Carica la directory dati"""
        primary = Path(__file__).parent.parent / "dati"
        fallback = Path(__file__).parent.parent.parent.parent / "dati"
        try:
            if primary.is_dir():
                return primary
            raise FileNotFoundError
        except FileNotFoundError:
            if fallback.is_dir():
                return fallback
            raise FileNotFoundError("Directory 'dati' non trovata.")

    def get_file_path(self, file_name: str):
        """Ritorna il percorso di un file nella directory dati"""
        try:
            return self.data_dir / file_name
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_name}' non trovato.")

    @staticmethod
    def read_csv_to_json(file_path: Path):
        """Legge un file CSV e ritorna i dati come lista di dizionari"""
        with open(file_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)

    def load_mini(self):
        """Ritorna i dati dei comuni filtrati per pro_com_t, comune e sigla"""

        def read_and_filter_data(file_path, keys):
            rows = self.read_csv_to_json(file_path)
            return [
                {k: row[k] for k in keys if k in row}
                for row in rows
            ]

        filtered = {"pro_com_t", "comune", "sigla"}
        main_data = read_and_filter_data(self.main_file, filtered)
        pop_data = read_and_filter_data(self.pop_file, filtered)

        merged_data = {m["pro_com_t"]: m for m in main_data if "pro_com_t" in m}
        for pop_item in pop_data:
            istat = pop_item.get("pro_com_t")
            if istat in merged_data:
                merged_data[istat].update(pop_item)
        return list(merged_data.values())

    def load_all(self):
        """Ritorna i dati dei comuni con tutti gli attributi disponibili"""
        main_data = self.read_csv_to_json(self.main_file)
        pop_data = self.read_csv_to_json(self.pop_file)

        merged_data = {}
        for item in main_data:
            istat = item.get("pro_com_t")
            if istat:
                merged_data[istat] = item

        for pop_item in pop_data:
            istat = pop_item.get("pro_com_t")
            if istat:
                if istat in merged_data:
                    merged_data[istat].update(pop_item)
                else:
                    merged_data[istat] = pop_item

        return list(merged_data.values())

    def load_map(self):
        """Ritorna i dati geografici dei comuni siciliani"""
        with open(self.map_file, mode="r", encoding="utf-8") as f:
            return json.load(f)
