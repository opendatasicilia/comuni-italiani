import React from "react";
import ReactDOM from "react-dom/client";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

import { Home } from "./pages";
import { GlobalStateProvider } from "./contexts/GlobalStateContext";
import "./style.css";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);

const queryClient = new QueryClient();

root.render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <GlobalStateProvider>
        <Home />
      </GlobalStateProvider>
    </QueryClientProvider>
  </React.StrictMode>
);
