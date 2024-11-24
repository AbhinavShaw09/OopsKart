


import { useNavigate } from "react-router-dom";
import { loginUser } from "../../api/auth";
import LoginForm from "../../components/LoginForm/LoginForm";
import { useAuth } from "../../context/AuthContext";

export const Login = () => {
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleLogin = async ({ username, password }) => {
    try {
      const data = await loginUser(username, password);

      login(data.access);

      localStorage.setItem("access_token", data.access);
      localStorage.setItem("refresh_token", data.refresh);

      navigate("/");
    } catch (error) {
      alert("Login failed: " + error.response?.data?.detail || error.message);
    }
  };

  return (
    <>
      <div>
        <LoginForm onSubmit={handleLogin} />
      </div>
    </>
  );
};
