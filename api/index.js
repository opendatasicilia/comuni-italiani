const express = require('express');
const csv=require('csvtojson')
const cors = require('cors');

const app = express();
const port = 8888;

const main = '../dati/main.csv'

const getData = (f) => {
    let file = csv().fromFile(f)
    return file
}

const getComune = async(comune) =>{
    const data = await getData(main)
    let place = data.filter(x => x.comune_codice_istat === comune)
    return place
}

app.use(cors({ origin: '*' }));

// Home
app.get('/', (req, res) => {
    res.send('Benvenuti');
});

// Tutti i comuni
app.get('/comuni', async (req, res) => {
    try {
        const data = await getData(main)
        res.send(data)
    }
    catch(e){
        console.log(e);
        res.sendStatus(e);
    }
})

// Comuni per codice ISTAT
app.get('/comuni/:istat', async (req, res) => {
    try {
        const data = await getComune(req.params.istat)
        res.send(data)
    }
    catch(e){
        console.log(e)
    }
});

app.listen(port, () => console.log(`Serving https://localhost:${port}`))