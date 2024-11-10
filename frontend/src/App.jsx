import { Route, Routes, useLocation } from "react-router-dom";

import { NavbarDefault } from "./components/Navbar";
import { Footer } from "./components/Footer";
import { Cart } from "./pages/Cart";
import { MarketPlace } from "./pages/MarketPlace";
import { Dashboard } from "./pages/Dashboard";
import { Login } from "./pages/Login";
import { Signup } from "./pages/Signup";

function App() {
  const location = useLocation();
  const hidePaths = ["/signup", "/login"];

  return (
    <>
      {!hidePaths.includes(location.pathname) && <NavbarDefault />}
      <Routes>
        <Route path="/" element={<MarketPlace />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
      {!hidePaths.includes(location.pathname) && <Footer />}
    </>
  );
}

export default App;
