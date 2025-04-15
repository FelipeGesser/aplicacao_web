import React, { useState } from "react";
import "./Login.css";
import { Link } from "react-router-dom";
import { loginUsuario } from "../funcoes/autenticaSenha"; // <- importa aqui

const Login = () => {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [erro, setErro] = useState("");

  const Logar = async () => {
    const { data, error } = await loginUsuario(email, senha);

    if (error) {
      setErro(error.message);
      console.error("Erro ao logar:", error.message);
    } else {
      console.log("Login feito com sucesso:", data);
      // redirecionar ou salvar token, etc.
    }
  };

  return (
    <div className="login-wrapper">
      <div className="login-container">
        <div className="login-box">
          <div className="user-icon">
            {/* ... seu SVG aqui */}
          </div>

          <div className="input-group">
            <input
              type="email"
              className="input-field"
              placeholder="Email"
              style={{ color: "white" }}
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          <div className="input-group">
            <input
              type="password"
              className="input-field"
              placeholder="Senha"
              style={{ color: "white" }}
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
            />
          </div>

          {erro && <p style={{ color: "red" }}>{erro}</p>}

          <p className="create-account">
            <Link to="/registrar">Criar conta</Link>
          </p>

          <button className="login-button" onClick={Logar}>
            Entrar
          </button>
        </div>
      </div>
    </div>
  );
};

export default Login;
