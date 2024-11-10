import { ProductList } from "../../api/ProductList";
import ProductListCard from "./ProductListCard";

const CONTENTS = ProductList;

export const ProductListSection = () => {
  return (
    <section className="py-10 px-8 flex flex-col min-h-screen">
      <div className="mx-auto container">
        <div className="grid grid-cols-1 gap-8 lg:grid-cols-3 md:grid-cols-2">
          {CONTENTS.map(({ img, name, price }, index) => (
            <ProductListCard key={index} img={img} name={name} price={price} />
          ))}
        </div>
      </div>
    </section>
  );
};
