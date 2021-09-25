Qui raccogliamo tutti i files .csv (anagrafiche, dati su popolazione, lat, long, codici istat, email)

A questo file verrà aggiunto lo schema dati dei csv caricati nella cartella dati

## Cosa contiene questa cartella 
- coordinate.csv
- stemmi.csv
- popolazione_2021.csv
- comuni.csv
- main.csv

## Struttura dei dati
Di seguito viene descritta la struttura dei files .csv

### coordinate.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
comune_codice_istat | Codice ISTAT del Comune | Numero | 001001
lat | Latitudine | WGS84 | 45.367055
long | Longitudine | WGS84 | 7.766918

### stemmi.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
comune_codice_istat | Codice ISTAT del Comune | Numero | 001001
stemma | Link all'immagine dello stemma del comune | Testo | https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/img/stemmi_cod_istat/001001.jpg

### popolazione_2021.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
comune_codice_istat | Codice ISTAT del Comune | Numero | 001001
popolazione | Popolazione | Numero | 2548

### comuni.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
comune_denominazione | Denominazione del comune | Testo | Agliè
comune_codice_istat | Codice ISTAT del Comune | Numero | 001001
provincia_denominazione | Denominazione della Provincia | Testo | Torino
provincia_sigla | Sigla della Provincia | Testo | TO
regione_denominazione | Denominazione della Regione | Testo | Piemonte
regione_codice | Codice ISTAT della regione | Numero | 1

### main.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
comune_denominazione | Denominazione del comune | Testo | Agliè
comune_codice_istat | Codice ISTAT del Comune | Numero | 001001
lat | Latitudine | WGS84 | 45.367055
long | Longitudine | WGS84 | 7.766918
provincia_denominazione | Denominazione della Provincia | Testo | Torino
provincia_sigla | Sigla della Provincia | Testo | TO
regione_denominazione | Denominazione della Regione | Testo | Piemonte
regione_codice | Codice ISTAT della regione | Numero | 1
stemma | Link all'immagine dello stemma del comune | Testo | https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/img/stemmi_cod_istat/001001.jpg
