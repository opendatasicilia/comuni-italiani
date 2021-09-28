import React, { useState, useEffect, useCallback } from "react";
import log from '../assets/imgs/opendatasicilia.png'
import axios from 'axios';

export default function Vax({istat}){
    const [isLoading,setIsLoading] = useState(true)
    const [data, setData] = useState(null);

    const getComune = useCallback(async () => {
        axios.get(`comuni/${istat}`)
            .then((res) => {
                setData(res.data)
                setIsLoading(false)
            })
            .catch((e) => {
                alert(e)
            })
        }, [istat])

    useEffect(() => {
        getComune()
    }, [getComune])

    return(
        isLoading ? 'Caricamento...' :
        <div>
            {!data ? <div style={{textAlign:'center'}}><img className='stemma' src={log} alt='OpenDataSicilia' /></div> :
                data &&
                <div className='comune'>
                    <img className='stemma' src={data.stemma} alt={data.comune} />
                    <h3>Comune di {data.comune}</h3>
                    <p>Popolazione: {data.pop_res_21} abitanti <small>(Istat, 2021)</small></p>
                    <p>Codice ISTAT: {data.pro_com_t}</p>
                    <p>CAP: {data.cap}</p>
                    <p>CF: {data.cf}</p>
                    <p>Provincia: {data.den_prov} ({data.sigla})</p>
                    <p>Regione: {data.den_reg}</p>
                    <p>Codice Regione: {data.cod_reg}</p>
                    <p>Coordinate: <a href={`https://umap.openstreetmap.fr/en/map/comuni-italiani-2021_660870#14/${data.lat}/${data.long}`} target='_blank' rel='noreferrer'>{data.lat}, {data.long}</a></p>
                    {data.mail ? <p>Email: <a href={`mailto:${data.mail}`}>{data.mail}</a></p> :null}
                    {data.pec ? <p>PEC: <a href={`mailto:${data.pec}`}>{data.pec}</a></p> :null}
                    {data.sito_web ? <p>Sito Web: <a href={data.sito_web} target='_blank' rel='noreferrer'>{data.sito_web}</a></p> :null}
                    {data.wikipedia ? <p>Wikipedia: <a href={data.wikipedia} target='_blank' rel='noreferrer'>{data.wikipedia}</a></p> :null}
                </div>
            }
        </div>
    )
}