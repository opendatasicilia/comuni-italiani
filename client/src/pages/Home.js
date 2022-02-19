import axios from 'axios';
import Loader from "react-loader-spinner";
import MenuList from "../components/MenuList";
import React, {useState, useEffect, useCallback} from 'react';
import Select, { createFilter } from "react-select";

import Comune from './Comune'

function App() {
  let options
  const [data, setData] = useState(null)
  const [istat, setIstat] = useState(null)
  const [isLoading, setIsLoading] = useState(true)

  const getComuni = useCallback(async () => {
    const response = await axios.get(`https://api.infocomuni.eu/comuni`)
    setData(response.data)
        setIsLoading(false)
    },[])

  useEffect(() => {
    getComuni()
  }, [getComuni])

  if(data){
    options = data.map(comune => (
      {
        value: comune.pro_com_t,
        label: comune.comune + " (" + comune.sigla + ")"
      } 
    ));    
  } else {
    options = [
      {
        value: 'Loading',
        label: 'Loading'
      }
    ]
  }
  const handleChange = (selectedOption) => {
    setIstat(selectedOption.value)
  };

  return (
    <div className='container mt-5 mb-5 App-header'>
      {
        isLoading ?
        <div className='App-header'>
          <Loader style={{position:'absolute', top:'50%'}}type="Rings" color="#0063C6" height={40} width={40} />
        </div>
        :
        <>
        <div className="col-12 col-md-4">
          <Select
            filterOption={createFilter({ ignoreAccents: false })}
            options={options}
            onChange={handleChange}
            components={{MenuList}}
            placeholder={'Inserisci nome del Comune'} 
          />
        </div>
        <div className='col-12'>
          <Comune istat={istat}/>
        </div>
        </>
      }
    </div>
  );
}

export default App;
