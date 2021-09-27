## Cosa contiene questa cartella 
- coordinate.csv
- stemmi.csv
- popolazione_2021.csv
- comuni.csv
- sito_web.csv
- pec.csv
- codice_ficale.csv
- cap.csv
- wikipedia.csv
- main.csv

## Struttura dei dati
Di seguito viene descritta la struttura dei files .csv

### coordinate.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune (pro_com_t) | Numero | 001001
lat | Latitudine | WGS84 | 45.367055
long | Longitudine | WGS84 | 7.766918

### stemmi.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune (pro_com_t) | Numero | 001001
stemma | Link all'immagine dello stemma del comune | Testo | https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/img/stemmi_cod_istat/001001.jpg

### popolazione_2021.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune (pro_com_t) | Numero | 001001
popolazione | Popolazione | Numero | 2548

### comuni.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
comune | Denominazione del comune | Testo | Agliè
pro_com_t | Codice ISTAT del Comune | Numero | 001001
den_prov | Denominazione della Provincia | Testo | Torino
sigla | Sigla della Provincia | Testo | TO
den_reg | Denominazione della Regione | Testo | Piemonte
cod_reg | Codice ISTAT della regione | Numero | 1

### sito_web.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
sito_web | Sito istituzionale del Comune | Testo | http://comune.aglie.to.it

### pec.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
pec | Indirizzo PEC dell'Ente | Testo | protocollo@pec.comune.aglie.to.it

### codice_fiscale.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
cf | Codice fiscale del Comune | Numero | 83501790014

### cap.cav
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
cap | Codice di Avviamento Postale del Comune dell'ente | Numero | 10011

### wikipedia.csv
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Numero | 001001
wikipedia | Link alla pagina wikipedia del Comune | Testo | https://it.wikipedia.org/wiki/Agliè

### main.csv
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
sito_web | Sito istituzionale del Comune | Testo | http://comune.aglie.to.it
wikipedia | Link alla pagina wikipedia del Comune | Testo | https://it.wikipedia.org/wiki/Agliè
stemma | Link all'immagine dello stemma del comune | Testo | https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/img/stemmi_cod_istat/001001.jpg
