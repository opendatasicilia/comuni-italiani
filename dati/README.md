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
- `wikidata.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/wikidata.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#wikidatacsv)) 
- `mail.csv`([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/mail.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#mailcsv))
- `main.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/main.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#maincsv))
- `ISTAT_popolazione_2021.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/ISTAT_popolazione_2021.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#istat_popolazione_2021csv))
- `comuni_codici-catastali.csv` ([file](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/comuni_codici-catastali.csv) | [schema dati](https://github.com/opendatasicilia/comuni-italiani/blob/main/dati/README.md#comuni_codici-catastalicsv))

## Fonti
- Amministrazioni:[ indicepa.gov.it](https://indicepa.gov.it/ipa-dati/dataset/amministrazioni)
- Popolazione: 
  - [Istat](https://www.istat.it/)
  - [Istat](http://demo.istat.it/pop2021/dati/comuni.zip)
- Codici statistici delle unità Amministrative territoriali:
  - [Istat](https://www.istat.it/it/archivio/6789)
- Stemmi: [araldicacivica.it](https://www.araldicacivica.it/) e [Wikipedia Italia](https://it.wikipedia.org/wiki/Pagina_principale/)

## Struttura dei dati
Di seguito viene descritta la struttura dei file .csv

### [coordinate.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/coordinate.csv)

Il centroide delle coordinate qui indicate si riferisce al Municipio del Comune interessato, e rispetta lo standard `EPSG:4326`

Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
lat | Latitudine | WGS84 | 45.367055
long | Longitudine | WGS84 | 7.766918

### [stemmi.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/stemmi.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
stemma | Link all'immagine dello stemma del comune | Testo | https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/img/stemmi_cod_istat/001001.jpg

### [popolazione_2021.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/popolazione_2021.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
pop_res_21 | Popolazione | Numero | 2548

### [comuni.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/comuni.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
comune | Denominazione del comune | Testo | Agliè
pro_com_t | Codice ISTAT del Comune | Testo | 001001
den_prov | Denominazione della Provincia | Testo | Torino
sigla | Sigla della Provincia | Testo | TO
den_reg | Denominazione della Regione | Testo | Piemonte
cod_reg | Codice ISTAT della regione | Numero | 1

### [sito_web.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/sito_web.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
sito_web | Sito istituzionale del Comune | Testo | http://comune.aglie.to.it

### [pec.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/pec.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
pec | Indirizzo PEC dell'Ente | Testo | protocollo@pec.comune.aglie.to.it

### [codice_fiscale.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/codice_fiscale.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
cf | Codice fiscale del Comune | Numero | 83501790014

### [cap.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/cap.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
cap | Codice di Avviamento Postale del Comune dell'ente | Numero | 10011

### [wikipedia.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/wikipedia.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
wikipedia | Link alla pagina wikipedia del Comune | Testo | https://it.wikipedia.org/wiki/Agliè

### [wikidata.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/wikidata.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
wikidata | Link alla pagina wikidata del Comune | Testo | http://www.wikidata.org/entity/Q8971

### [ISTAT_popolazione_2021.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/ISTAT_popolazione_2021.csv)

Popolazione residente per Comune di Italia, aggiornata a gennaio 2021. Fonte: [Istat](http://demo.istat.it/pop2021/dati/comuni.zip).

Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
<12 | numero di residenti per Comune di età inferiore a 5 anni  | Numero | 122
\>=12 | numero di residenti per Comune con età maggiore o uguale a 5 anni  | Numero | 223
totale | numero di residenti totale per Comune | Numero | 12

### [comuni_codici-catastali.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/comuni_codici-catastali.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
codice_catastale | Codice Catastale del comune | testo | A074
comune | Denominazione del comune | testo | Agliè

### [target5.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/target5.csv)

Popolazione residente per Comune di Italia, aggiornata a (?) 2021. Fonte: [Istat](http://demo.istat.it/pop2021/dati/comuni.zip).

Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
<5 | numero di residenti per Comune di età inferiore a 5 anni  | Numero | 122
\>=5 | numero di residenti per Comune con età maggiore o uguale a 5 anni  | Numero | 223
totale | numero di residenti totale per Comune | Numero | 12

### [mail.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/mail.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
pro_com_t | Codice ISTAT del Comune | Testo | 001001
mail | Indirizzo email dell'Ente | testo | protocollo@pec.comune.aglie.to.it

### [main.csv](https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/main.csv)
Nome campo | Descrizione | Formato | Esempio
-- | -- | -- | --
comune | Denominazione del comune | Testo | Agliè
pro_com_t | Codice ISTAT del Comune | Testo | 001001
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
