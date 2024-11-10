import { useFetch } from "../../hooks/useFetch";
import { Spinner } from "@material-tailwind/react";
import {ProductListSection} from "./ProductListSection"; 

export const MarketPlace = () => {
  const { data, loading, error } = useFetch(
    "http://127.0.0.1:8000/api/products/"
  );

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <Spinner className="h-16 w-16 text-gray-900/50" />
      </div>
    );
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }
  return <ProductListSection/>;
};
