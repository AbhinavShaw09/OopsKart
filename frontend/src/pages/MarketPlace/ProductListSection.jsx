import ProductListCard from "./ProductListCard";

export const ProductListSection = ({ data }) => {
  return (
    <section className="py-10 px-8 flex flex-col min-h-screen">
      <div className="mx-auto container">
        <div className="grid grid-cols-1 gap-8 lg:grid-cols-3 md:grid-cols-2">
          {data.map(({ img, name, price }, index) => (
            <ProductListCard key={index} img={img} name={name} price={price} />
          ))}
        </div>
      </div>
    </section>
  );
};
