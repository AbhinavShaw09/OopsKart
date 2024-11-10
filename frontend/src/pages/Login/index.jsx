import { Link } from "react-router-dom";
import { Typography } from "@material-tailwind/react";
export const Login = () => {
  return (
    <>
      <Typography
        as="li"
        variant="small"
        color="blue-gray"
        className="flex items-center gap-x-2 p-1 font-medium"
      >
        <Link to="/" className="flex items-center">
          Login
        </Link>
      </Typography>
    </>
  );
};
