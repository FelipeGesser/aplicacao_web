import React, { useState } from "react";
import "./recupera.css";
import { Link } from "react-router-dom";
import { recuperarSenha } from "../funcoes/recuperar";;

const Recupera = () => {
  const [email, setEmail] = useState("");
  const [mensagem, setMensagem] = useState("");
  const [erro, setErro] = useState("");

  const handleEnviarCodigo = async (e) => {
    e.preventDefault();
    setMensagem("");
    setErro("");

    const { data, error } = await recuperarSenha(email);

    if (error) {
      setErro(error.message);
    } else {
      setMensagem("E-mail de recuperação enviado! Verifique sua caixa de entrada.");
    }
  };

  return (
    <div className="recupera-container">
      <h2>Recuperar Senha</h2>
      <form onSubmit={handleEnviarCodigo}>
        <input
          type="email"
          className="input-field"
          placeholder="Digite seu e-mail"
          value={email}
          onChange={e => setEmail(e.target.value)}
          required
        />
        <button type="submit" className="login-button">
          Enviar Código
        </button>
      </form>

      {mensagem && <p style={{ color: "#4caf50", marginTop: "1rem" }}>{mensagem}</p>}
      {erro    && <p style={{ color: "#f44336", marginTop: "1rem" }}>{erro}</p>}

      <Link to="/" className="create-account" style={{ marginTop: "16px" }}>
        Voltar ao login
      </Link>
    </div>
  );
};

export default Recupera;
