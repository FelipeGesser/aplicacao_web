import React, { useState } from "react";
import "./Registrar.css";
import { Link, useNavigate } from "react-router-dom";
import { registrarUsuario } from "../funcoes/criarUsuario";

const Registrar = () => {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [confirmaSenha, setConfirmaSenha] = useState("");
  const [erro, setErro] = useState("");
  const navigate = useNavigate();

  const Registro = async () => {
    setErro("");

    if (senha !== confirmaSenha) {
      setErro("As senhas não coincidem.");
      return;
    }

    const { data, error } = await registrarUsuario(email, senha);

    if (error) {
      setErro(error.message);
    } else {
      console.log("Conta criada:", data);
      navigate("/"); // redireciona pro login
    }
  };

  return (
    <div className="registrar-wrapper">
      <div className="registrar-container">
        <div className="registrar-box">
          <div className="user-icon">
            {/* SVG do ícone */}
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="user-svg"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <circle cx="12" cy="8" r="4" />
              <path d="M16 16a4 4 0 0 0-8 0" />
            </svg>
          </div>

          <div className="input-group">
            <input
              type="email"
              className="input-field"
              placeholder="E-mail"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          <div className="input-group">
            <input
              type="password"
              className="input-field"
              placeholder="Senha"
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
            />
          </div>

          <div className="input-group">
            <input
              type="password"
              className="input-field"
              placeholder="Confirmar senha"
              value={confirmaSenha}
              onChange={(e) => setConfirmaSenha(e.target.value)}
            />
          </div>

          {erro && <p style={{ color: "red" }}>{erro}</p>}

          <p className="create-account">
            <Link to="/">Já tenho uma conta</Link>
          </p>

          <button className="registrar-button" onClick={Registro}>
            Criar
          </button>
        </div>
      </div>
    </div>
  );
};

export default Registrar;
