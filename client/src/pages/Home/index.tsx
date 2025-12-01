import { useMemo } from "react";

import { Comune } from "../Comune";
import { TComune } from "../../utils/types";
import { useAPI } from "../../hooks/useAPI";
import { useGlobalState } from "../../hooks/useGlobalState";
import { Loader, SearchBar } from "../../components";

export const Home = () => {
  const { selectedComune, setComune, clearComune } = useGlobalState();

  const {
    data: comuni,
    isLoading,
    isError,
  } = useAPI<TComune[]>("comuni", "/comuni");

  const comuniOptions = useMemo(() => {
    if (!comuni) return [];
    return comuni.map((comune) => ({
      id: comune.pro_com_t,
      value: comune.pro_com_t,
      name: comune.comune + " (" + comune.sigla + ")",
    }));
  }, [comuni]);

  if (isLoading) return <Loader className="vh-100" />;

  if (isError)
    return (
      <div className="d-flex justify-content-center align-items-center vh-100">
        <p>Errore nel caricamento dei comuni.</p>
      </div>
    );

  return (
    <div className="container mt-5 mb-5 App-header">
      <div className="col-12 col-md-4">
        <SearchBar
          options={comuniOptions}
          onSelect={setComune}
          onClear={clearComune}
          autoFocus={!selectedComune}
        />
      </div>
      <div className="col-12">
        <Comune istat={selectedComune?.value} />
      </div>
    </div>
  );
};
