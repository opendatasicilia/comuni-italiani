import { Fragment } from "react";

import { IComune, TComune } from "../../utils/types";
import { fieldFormatters } from "./utils";
import { useAPI } from "../../hooks/useAPI";

import log from "../../assets/imgs/opendatasicilia.png";
import { Loader } from "../../components/Loader";

export const Comune = ({ istat }: IComune) => {
  const {
    data: comune,
    isLoading,
    isError,
  } = useAPI<TComune>(
    ["comune", istat],
    `/comuni/${istat}`,
    undefined,
    !!istat
  );

  if (isLoading) return <Loader className="mt-5" />;

  if (isError)
    return (
      <div className="d-flex justify-content-center align-items-center vh-100">
        <p>Errore nel caricamento del comune.</p>
      </div>
    );

  return comune ? (
    <div className="comune">
      {Object.keys(fieldFormatters).map((key) => {
        const k = key as keyof TComune;
        return (
          <Fragment key={k}>{fieldFormatters[k](comune[k], comune)}</Fragment>
        );
      })}
    </div>
  ) : (
    <div className="text-center">
      <img className="stemma" src={log} alt="OpenDataSicilia" />
    </div>
  );
};
