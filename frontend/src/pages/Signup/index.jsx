import { useNavigate } from "react-router-dom";
import { signUpUser } from "../../api/auth";
import  SignUpForm  from "../../components/SignUpForm/SignUpForm";

const SignUpPage = () => {
  const navigate = useNavigate();

  const handleSignup = async ({ username, password, email }) => {
    try {
      await signUpUser(username, password, email);
      navigate("/login");
    } catch (error) {
      alert("Signup failed: " + error.response?.data?.detail || error.message);
    }
  };

  return (
    <div>
      <h2>Signup</h2>
      <SignUpForm onSubmit={handleSignup} />
    </div>
  );
};

export default SignUpPage;
