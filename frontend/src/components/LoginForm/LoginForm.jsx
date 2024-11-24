import { useState } from "react";
import {
  Card,
  Input,
  Button,
  CardBody,
  CardHeader,
  Typography,
} from "@material-tailwind/react";

const LoginForm = ({ onSubmit }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ username, password });
  };

  return (
    <>
      <section className="px-8">
        <div className="container mx-auto h-screen grid place-items-center">
          <Card
            shadow={false}
            className="md:px-24 md:py-14 py-8 border border-gray-300"
          >
            <CardHeader shadow={false} floated={false} className="text-center">
              <Typography
                variant="h1"
                color="blue-gray"
                className="!text-3xl lg:text-4xl"
              >
                OopsKart
              </Typography>
            </CardHeader>
            <CardBody>
              <form
                onSubmit={handleSubmit}
                className="flex flex-col gap-4 md:mt-12"
              >
                <div>
                  <label>
                    <Typography
                      variant="small"
                      color="blue-gray"
                      className="block font-medium mb-2"
                      type="text"
                    >
                      Username
                    </Typography>
                  </label>
                  <Input
                    id="username"
                    color="gray"
                    size="lg"
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                    name="username"
                    placeholder="name@mail.com"
                    className="w-full placeholder:opacity-100 focus:border-t-primary border-t-blue-gray-200"
                    labelProps={{
                      className: "hidden",
                    }}
                  />
                </div>
                <div>
                  <label>
                    <Typography
                      variant="small"
                      color="blue-gray"
                      className="block font-medium mb-2"
                    >
                      Password
                    </Typography>
                  </label>
                  <Input
                    id="password"
                    color="gray"
                    size="lg"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    name="password"
                    placeholder="password"
                    className="w-full placeholder:opacity-100 focus:border-t-primary border-t-blue-gray-200"
                    labelProps={{
                      className: "hidden",
                    }}
                  />
                </div>
                <Button size="lg" color="gray" fullWidth type="submit">
                  Login
                </Button>
                <Button
                  variant="outlined"
                  size="lg"
                  className="flex h-12 border-blue-gray-200 items-center justify-center gap-2"
                  fullWidth
                >
                  <img
                    src={`https://www.material-tailwind.com/logos/logo-google.png`}
                    alt="google"
                    className="h-6 w-6"
                  />{" "}
                  sign in with google
                </Button>

                <Typography
                  variant="small"
                  className="text-center mx-auto max-w-[19rem] !font-medium !text-gray-600"
                >
                  Upon signing in, you consent to abide by our{" "}
                  <a href="#" className="text-gray-900">
                    Terms of Service
                  </a>{" "}
                  &{" "}
                  <a href="#" className="text-gray-900">
                    Privacy Policy.
                  </a>
                </Typography>
              </form>
            </CardBody>
          </Card>
        </div>
      </section>
    </>
  );
};

export default LoginForm;
