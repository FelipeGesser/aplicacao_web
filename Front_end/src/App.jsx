import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Registrar from "./pages/Registrar";
import Recupera from "./pages/recupera";
import UpdatePassword from "./pages/atualizasenha";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/registrar" element={<Registrar />} />
        <Route path="/recupera" element={<Recupera />} />
        <Route path="/atualizasenha" element={<UpdatePassword />} />
      </Routes>
    </Router>
  );
}

export default App;
