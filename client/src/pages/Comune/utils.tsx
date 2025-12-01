import { JSX } from "react";
import { TComune } from "../../utils/types";

type Formatter = (
  value: TComune[keyof TComune],
  data: TComune
) => JSX.Element | string | null;

export const fieldFormatters: Record<keyof TComune, Formatter> = {
  stemma: (value) => (
    <img className="stemma" src={value as string} alt="Stem" />
  ),
  comune: (value) => <h3>Comune di {value}</h3>,
  pop_res_21: (value) => (
    <p>
      Popolazione: {value} abitanti <small>(Istat, 2021)</small>
    </p>
  ),
  pro_com_t: (value) => <p>Codice ISTAT: {value}</p>,
  cap: (value) => <p>CAP: {value}</p>,
  cf: (value) => <p>CF: {value}</p>,
  den_prov: (value, data) => (
    <p>
      Provincia: {value} ({data.sigla})
    </p>
  ),
  sigla: () => null,
  den_reg: (value) => <p>Regione: {value}</p>,
  cod_reg: (value) => <p>Codice Regione: {value}</p>,
  lat: (value, data) => (
    <p>
      Coordinate:{" "}
      <a
        href={`https://umap.openstreetmap.fr/en/map/comuni-italiani-2021_660870#14/${data.lat}/${data.long}`}
        target="_blank"
        rel="noreferrer"
      >
        {data.lat}, {data.long}
      </a>
    </p>
  ),
  long: () => null,
  mail: (value) =>
    value ? (
      <p>
        Email: <a href={`mailto:${value}`}>{value}</a>
      </p>
    ) : null,
  pec: (value) =>
    value ? (
      <p>
        PEC: <a href={`mailto:${value}`}>{value}</a>
      </p>
    ) : null,
  sito_web: (value) =>
    value ? (
      <p>
        Sito Web:{" "}
        <a href={value as string} target="_blank" rel="noreferrer">
          {value}
        </a>
      </p>
    ) : null,
  wikipedia: (value) =>
    value ? (
      <p>
        Wikipedia:{" "}
        <a href={value as string} target="_blank" rel="noreferrer">
          {value}
        </a>
      </p>
    ) : null,
};
