import { Typography } from "@material-tailwind/react";
import { Link } from "react-router-dom";


export const navList = (
  <ul className="mt-2 mb-4 flex flex-col gap-2 lg:mb-0 lg:mt-0 lg:flex-row lg:items-center lg:gap-6">
    <Typography
      as="li"
      variant="small"
      color="blue-gray"
      className="flex items-center gap-x-2 p-1 font-medium"
    >
      <Link to="/" className="flex items-center">
        Market Place
      </Link>
    </Typography>
    <Typography
      as="li"
      variant="small"
      color="blue-gray"
      className="flex items-center gap-x-2 p-1 font-medium"
    >
      <Link to="/cart" className="flex items-center">
        Cart
      </Link>
    </Typography>
    <Typography
      as="li"
      variant="small"
      color="blue-gray"
      className="flex items-center gap-x-2 p-1 font-medium"
    >
      <Link to="/dashboard" className="flex items-center">
      Dashboard
      </Link>
    </Typography>
  </ul>
);
