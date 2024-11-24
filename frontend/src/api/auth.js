import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api";

export const loginUser = async (username, password) => {
  const response = await axios.post(`${API_BASE_URL}/login/`, {
    username,
    password,
  });
  return response.data;
};

export const signUpUser = async (username, password, email) => {
  const response = await axios.post(`${API_BASE_URL}/signup/`, {
    username,
    password,
    email,
  });
  return response.data;
};
