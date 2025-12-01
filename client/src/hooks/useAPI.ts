import { useQuery } from "@tanstack/react-query";
import axios, { AxiosRequestConfig } from "axios";
import { BASE_URL } from "../utils/constants";

const fetchAPI = async <T>(
  url: string,
  config?: AxiosRequestConfig
): Promise<T> => {
  const { data } = await axios.get<T>(`${BASE_URL}${url}`, config);
  return data;
};

export const useAPI = <T>(
  key: string | readonly unknown[],
  url: string,
  config?: AxiosRequestConfig,
  enabled = true
) => {
  return useQuery<T>({
    queryKey: Array.isArray(key) ? key : [key],
    queryFn: () => fetchAPI<T>(url, config),
    enabled,
    staleTime: 5 * 60 * 1000,
    retry: 1,
  });
};
