import React, { createContext, useReducer, ReactNode } from "react";
import {
  TGlobalState,
  TGlobalStateAction,
  TGlobalStateContextValue,
} from "../utils/types";

const initialState: TGlobalState = {
  selectedComune: undefined,
};

const reducer = (
  state: TGlobalState,
  action: TGlobalStateAction
): TGlobalState => {
  switch (action.type) {
    case "SET_COMUNE":
      return {
        ...state,
        selectedComune: action.payload,
      };
    case "CLEAR_COMUNE":
      return {
        ...state,
        selectedComune: undefined,
      };
    default:
      return state;
  }
};

export const GlobalStateContext = createContext<
  TGlobalStateContextValue | undefined
>(undefined);

interface GlobalStateProviderProps {
  children: ReactNode;
}

export const GlobalStateProvider: React.FC<GlobalStateProviderProps> = ({
  children,
}) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <GlobalStateContext.Provider value={{ state, dispatch }}>
      {children}
    </GlobalStateContext.Provider>
  );
};
