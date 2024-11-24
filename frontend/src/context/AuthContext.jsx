import { createContext, useContext, useState, useEffect } from "react";

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null); 
  const [token, setToken] = useState(
    localStorage.getItem("access_token") || null
  );

  const login = ( accessToken) => {
    setToken(accessToken);
    localStorage.setItem("access_token", accessToken);
  };


  const logout = () => {
    setToken(null);
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
  };

  useEffect(() => {
    if (token) {
      const savedUser = JSON.parse(localStorage.getItem("user") || "{}");
      setUser(savedUser);
    }
  }, [token]);

  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
