import { ReactSearchAutocomplete } from "react-search-autocomplete";
import { TComuneSearchItem } from "../../utils/types";

interface SearchBarProps {
  options: TComuneSearchItem[];
  onSelect: (item: TComuneSearchItem) => void;
  onClear: () => void;
  autoFocus?: boolean;
}

export const SearchBar = ({
  options,
  onSelect,
  onClear,
  autoFocus,
}: SearchBarProps) => {
  return (
    <ReactSearchAutocomplete
      items={options}
      fuseOptions={{ keys: ["name"] }}
      placeholder="Inserisci nome del Comune"
      showNoResultsText="Nessun risultato"
      onSelect={(item) => onSelect(item)}
      onClear={() => onClear()}
      autoFocus={autoFocus}
      maxResults={10}
    />
  );
};
