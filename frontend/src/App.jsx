import { Route, Routes } from "react-router-dom";

import { NavbarDefault } from "./components/Navbar";
import { Checkout } from "./pages/Checkout";
import { MarketPlace } from "./pages/MarketPlace";
import { Dashboard } from "./pages/Dashboard";

function App() {
  return (
    <>
      <NavbarDefault />
      <Routes>
        <Route path="/" element={<MarketPlace />} />
        <Route path="/checkout" element={<Checkout />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </>
  );
}

export default App;
