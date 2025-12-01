type TComune = {
  stemma: string;
  comune: string;
  pop_res_21: number;
  pro_com_t: string;
  cap: string;
  cf: string;
  den_prov: string;
  sigla: string;
  den_reg: string;
  cod_reg: string;
  lat: number;
  long: number;
  mail?: string;
  pec?: string;
  sito_web?: string;
  wikipedia?: string;
};

interface IComune {
  istat?: string;
}

type TComuneSearchItem = {
  id: string;
  value: string;
  name: string;
};

type TGlobalState = {
  selectedComune: TComuneSearchItem | undefined;
};

type TGlobalStateAction =
  | { type: "SET_COMUNE"; payload: TComuneSearchItem | undefined }
  | { type: "CLEAR_COMUNE" };

type TGlobalStateContextValue = {
  state: TGlobalState;
  dispatch: React.Dispatch<TGlobalStateAction>;
};

export type {
  TComune,
  IComune,
  TComuneSearchItem,
  TGlobalState,
  TGlobalStateAction,
  TGlobalStateContextValue,
};
