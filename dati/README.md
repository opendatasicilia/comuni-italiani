## Cosa contiene questa cartella 
- `coordinate.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/coordinate.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#coordinatecsv))
- `stemmi.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/stemmi.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#stemmicsv))
- `popolazione_2021.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/popolazione_2021.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#popolazione_2021csv))
- `comuni.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/comuni.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#comunicsv))
- `sito_web.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/sito_web.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#sito_webcsv))
- `pec.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/pec.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#peccsv))
- `codice_ficale.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/codice_fiscale.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#codice_fiscalecsv))
- `cap.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/cap.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#capcsv))
- `wikipedia.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/wikipedia.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#wikipediacsv))
- `mail.csv`([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/mail.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#mailcsv))
- `main.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/main.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#maincsv))

## Struttura dei dati
Di seguito viene descritta la struttura dei files .csv

### [coordinate.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/coordinate.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
lat | Latitudine | WGS84 | 45.367055
long | Longitudine | WGS84 | 7.766918

### [stemmi.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/stemmi.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
stemma | Link all'immagine dello stemma del comune | Testo | https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/img/stemmi_cod_istat/001001.jpg

### [popolazione_2021.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/popolazione_2021.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
popolazione | Popolazione | Numero | 2548

### [comuni.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/comuni.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
comune | Denominazione del comune | Testo | Agliè
pro_com_t | Codice ISTAT del Comune | Numero | 001001
den_prov | Denominazione della Provincia | Testo | Torino
sigla | Sigla della Provincia | Testo | TO
den_reg | Denominazione della Regione | Testo | Piemonte
cod_reg | Codice ISTAT della regione | Numero | 1

### [sito_web.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/sito_web.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
sito_web | Sito istituzionale del Comune | Testo | http://comune.aglie.to.it

### [pec.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/pec.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
pec | Indirizzo PEC dell'Ente | Testo | protocollo@pec.comune.aglie.to.it

### [codice_fiscale.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/codice_fiscale.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
cf | Codice fiscale del Comune | Numero | 83501790014

### [cap.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/cap.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
cap | Codice di Avviamento Postale del Comune dell'ente | Numero | 10011

### [wikipedia.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/wikipedia.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
wikipedia | Link alla pagina wikipedia del Comune | Testo | https://it.wikipedia.org/wiki/Agliè

### [mail.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/mail.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
mail | Indirizzo email dell'Ente | testo | protocollo@pec.comune.aglie.to.it

### [main.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/main.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
comune | Denominazione del comune | Testo | Agliè
pro_com_t | Codice ISTAT del Comune | Numero | 001001
lat | Latitudine | WGS84 | 45.367055
long | Longitudine | WGS84 | 7.766918
den_prov | Denominazione della Provincia | Testo | Torino
sigla | Sigla della Provincia | Testo | TO
den_reg | Denominazione della Regione | Testo | Piemonte
cod_reg | Codice ISTAT della regione | Numero | 1
cap | Codice di Avviamento Postale del Comune dell'ente | Numero | 10011
cf | Codice fiscale del Comune | Numero | 83501790014
pec | Indirizzo PEC dell'Ente | Testo | protocollo@pec.comune.aglie.to.it
mail | Indirizzo email dell'Ente | testo | protocollo@pec.comune.aglie.to.it
sito_web | Sito istituzionale del Comune | Testo | http://comune.aglie.to.it
wikipedia | Link alla pagina wikipedia del Comune | Testo | https://it.wikipedia.org/wiki/Agliè
stemma | Link all'immagine dello stemma del comune | Testo | https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/img/stemmi_cod_istat/001001.jpg
