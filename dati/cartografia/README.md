Qui raccogliamo tutti i link alla cartografia [ISTAT](https://www.istat.it/it/)

# Confini delle unità amministrative a fini statistici

Tutti i dati dei [confini delle unità amministrative](https://www.istat.it/it/archivio/222527) a fini statistici sono diffusi annualmente, a partire dal 2002 con riferimenti al 1° gennaio dell’anno in corso, in un formato uniforme per strato informativo, come specificato nel documento di descrizione dei dati. Le sole eccezioni temporali riguardano i dati degli anni censuari (1991, 2001 e 2011) diffusi alla data del censimento.

I confini delle unità amministrative a fini statistici sono costituiti da tre livelli gerarchici (regioni, province e comuni) e uno statistico (ripartizioni geografiche) a copertura nazionale, cui si aggiungono negli anni censuari anche le aree speciali (zone in contestazione e isole amministrative).

Il formato dei dati è shapefile nel sistema di riferimento WGS84; il dettaglio tecnico della proiezione è riportato nel file apposito (formato prj), associato a ciascun file geografico. La scala non è certificabile uniformemente dall’Istat, poichè le basi di acquisizione utilizzate (principalmente foto aeree ed altra cartografia) provengono da fonti e scale differenti, che variano tra ambito urbano ed ambito extraurbano.

I file geografici delle ripartizioni geografiche, regioni, province, città metropolitane e comuni includono:

- le modifiche nei limiti amministrativi segnalate e formalmente documentate dai comuni in occasione dell’aggiornamento delle basi territoriali per i censimenti 2010-11;
- le variazioni amministrative e territoriali intervenute nei periodi intercensuari consultabili nella sezione [Codici dei comuni, delle province e delle regioni](https://www.istat.it/it/archivio/6789);
- le variazioni amministrative, conseguenti alla risoluzione di zone in contestazione tra comuni limitrofi, nel periodo intercensuario, acquisite in seguito all’invio all’Istat della documentazione ufficiale e completa a corredo.

Gli attributi degli shapefile sono codificati (encoding) in UTF-8 come descritto nel relativo file di riferimento (formato cpg), collegato al dato geografico.

---

# Le basi geografiche e gli indicatori socio-economici dei nuovi collegi elettorali

Le [basi geografiche](https://www.istat.it/it/archivio/208278) (in formato shapefile) dei nuovi collegi elettorali per l’elezione dei rappresentanti parlamentari, pubblicate lo scorso 15 gennaio 2018, vengono integrate con un set di indicatori socio-economici calcolati per il 232 collegi uninominali e 63 collegi plurinominali per la Camera dei deputati e per i 116 collegi uninominali e 33 collegi plurinominali per il Senato della Repubblica.

---

# Basi territoriali e variabili censuarie

[Basi territoriali](https://www.istat.it/it/archivio/104317#Basiterritoriali-0) | [Confini amministrativi](https://www.istat.it/it/archivio/104317#Confiniamministrativi-1) | [Variabili censuarie](https://www.istat.it/it/archivio/104317#Variabilicensuarie-2) | [Dati toponomastici](https://www.istat.it/it/archivio/104317#Datitoponomastici-3)

L’Istat pubblica i dati geografici del sistema delle basi territoriali degli anni 1991, 2001 e 2011 dell’insieme delle partizioni e zonizzazioni del territorio italiano:

- Sezioni di censimento;
- Aree di censimento (solo nella versione 2011 e per i comuni maggiori di 20.000 abitanti o capoluogo di provincia al 1 gennaio 2008);
- Aree sub comunali (municipi, quartieri ecc. dei 34 comuni di maggiore dimensione demografica e con popolazione non inferiore a 100.000 abitanti);
- Località.
I dati geografici delle sezioni di censimento, mosaicati a livello nazionale, sono disponibili in duplice proiezione geografica (sistema di riferimento ED 1950 UTM Zona 32n e WGS 84 UTM Zona 32n) in formato shapefile. I dati del 2011 sono diffusi anche in formato kmz.

---

# Nuts Reposytory [OnData](https://github.com/ondata/nuts) 

La **suddivisione territoriale statistica standard** in Europa (EUROSTAT) è la [**NUTS**](https://www.wikiwand.com/it/Nomenclatura_delle_unit%C3%A0_territoriali_statistiche). In Italia è di particolare interesse in alcuni contesti, come ad esempio quello della **sanità**, per il quale il paese è suddiviso funzionalmente non nelle 20 regioni "classiche", ma nelle 21 zone `NUTS2` (il Trentino-Alto Adige suddiviso nelle due province autonome).

Una fonte classica per i file geografici con i limiti amministrativi è [**ISTAT**](https://www.istat.it/it/archivio/222527), che però **non pubblica** ad esempio **file "tagliati" secondo `NUTS2`** (è appunto il livello gerarchico regionale).<br>
Questo *[repository](https://github.com/ondata/nuts)* per raccogliere alcuni file geografici suddivisi secondo NUTS (al momento soltanto 2).

Abbiamo chiesto ad ISTAT di pubblicare file geografici anche secondo `NUTS2`: al momento non li pubblicheranno ma ci hanno suggerito una modalità per farlo in autonomia e si sono detti interessati a farlo nel futuro.<br>
È fondamentale per due ragioni:

- le [API ISTAT SDMX](https://www.istat.it/it/metodi-e-strumenti/web-service-sdmx) espongono le informazioni geografiche, secondo NUTS (📚 qui [la  guida ondata](https://ondata.github.io/guida-api-istat/)). Attenzione quelli qui esposti sono i codici nella codifica del 2006;
- come detto sopra, in alcuni contesti (sanità, scuola, protezione civile, ecc.) il taglio geografico non è quello regionale "classico", ma coincide proprio con il `NUTS2`.

**Maggiori dettagli nel repository [Nuts](https://github.com/ondata/nuts)**