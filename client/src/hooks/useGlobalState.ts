import { useContext, useCallback } from "react";
import { GlobalStateContext } from "../contexts/GlobalStateContext";
import { TComuneSearchItem } from "../utils/types";

export const useGlobalState = () => {
  const context = useContext(GlobalStateContext);

  if (!context) {
    throw new Error("useGlobalState must be used within GlobalStateProvider");
  }

  const { state, dispatch } = context;

  const setComune = useCallback(
    (comune: TComuneSearchItem | undefined) => {
      dispatch({ type: "SET_COMUNE", payload: comune });
    },
    [dispatch]
  );

  const clearComune = useCallback(() => {
    dispatch({ type: "CLEAR_COMUNE" });
  }, [dispatch]);

  return {
    selectedComune: state.selectedComune,
    setComune,
    clearComune,
  };
};
