import PropTypes from "prop-types";
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


ProductListSection.propTypes = {
  data: PropTypes.arrayOf(
    PropTypes.shape({
      img: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      price: PropTypes.oneOfType([PropTypes.number, PropTypes.string])
        .isRequired,
    })
  ).isRequired,
};
