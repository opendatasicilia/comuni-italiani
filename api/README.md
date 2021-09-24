# API Comuni

## **Quick Start:**

1. `yarn (or npm install)`
2. `node index.js`

## **Documentazione:**

**Tutti i Comuni**
Restituisce un array di oggetti in formato JSON con tutti i dati disponibili.

- **URL**
  /comuni

- **Metodo:**
  `GET`

---

**Singolo Comune per codice ISTAT**
Restituisce un oggetto in formato JSON con i dati relativi al Comune desiderato.

- **URL**
  /comuni/:istat

- **Metodo:**
  `GET`

- **Esempio:**
  ```bash
  $ curl -v http://localhost:8888/comuni/086019
  {
    "comune_denominazione": "Valguarnera Caropepe",
    "comune_codice_istat": "086019",
    "lat": "37.49542",
    "long": "14.390791",
    "provincia_denominazione": "Enna",
    "provincia_sigla": "EN",
    "regione_denominazione": "Sicilia",
    "regione_codice": "19",
    "stemma": "https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/img/stemmi_cod_istat/086019.png"
  }
  ```
