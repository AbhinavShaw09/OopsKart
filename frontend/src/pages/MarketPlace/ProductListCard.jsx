import {
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  Typography,
  Button,
} from "@material-tailwind/react";

const ProductListCard = ({ img, name, price }) => {
  return (
    <>
      <Card className="rounded-lg border border-gray-900 cursor-grab">
        <CardHeader shadow={false} floated={false} className="">
          <img
            src={img}
            alt="card-image"
            className="h-full= w-full object-cover p-4"
          />
        </CardHeader>
        <CardBody className="p-4">
          <div className="mb-2 flex items-center justify-between">
            <Typography color="blue-gray" className="font-medium">
              {name}
            </Typography>
            <Typography color="blue-gray" className="font-medium">
              {price}
            </Typography>
          </div>
          <Typography
            variant="small"
            color="gray"
            className="font-normal opacity-75"
          >
            With plenty of talk and listen time, voice-activated Siri access,
            and an available wireless charging case.
          </Typography>
        </CardBody>
        <CardFooter className="pt-0 flex items-center justify-center">
          <Button
            ripple={false}
            fullWidth={true}
            className="bg-gray-300 text-blue-gray-900 shadow-none hover:scale-105 hover:shadow-none focus:scale-105 focus:shadow-none active:scale-100 w-1/2 my-4 p-4"
          >
            Add to Cart
          </Button>
        </CardFooter>
      </Card>
    </>
  );
};

export default ProductListCard;
