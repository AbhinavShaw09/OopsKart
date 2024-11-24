import { Route, Routes, useLocation } from "react-router-dom";

import { NavbarDefault } from "./components/Navbar";
import { Footer } from "./components/Footer";
import { Cart } from "./pages/Cart";
import { MarketPlace } from "./pages/MarketPlace";
import { Login } from "./pages/Login";
import  SignUpPage  from "./pages/Signup";
import { AuthProvider } from "./context/AuthContext.jsx";
import  PrivateRoute  from "./utils/PrivateRoute";

function App() {
  const location = useLocation();
  const hidePaths = ["/signup", "/login"];

  return (
    <>
      <AuthProvider>
        {!hidePaths.includes(location.pathname) && <NavbarDefault />}
        <Routes>
          <Route
            path="/"
            element={
              <PrivateRoute>
                <MarketPlace />
              </PrivateRoute>
            }
          />
          <Route
            path="/cart"
            element={
              <PrivateRoute>
                <Cart />
              </PrivateRoute>
            }
          />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<SignUpPage />} />
        </Routes>
        {!hidePaths.includes(location.pathname) && <Footer />}
      </AuthProvider>
    </>
  );
}

export default App;
