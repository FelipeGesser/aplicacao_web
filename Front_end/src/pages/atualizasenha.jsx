import React, { useState, useEffect } from "react";
import { useSearchParams, useNavigate } from "react-router-dom";
import { atualizarSenha } from "../funcoes/atualizasenhas";
import "./atualizasenha.css";

export default function UpdatePassword() {
  const [searchParams] = useSearchParams();
  const accessToken = searchParams.get("access_token") || "";
  const navigate = useNavigate();

  const [senha, setSenha] = useState("");
  const [confirma, setConfirma] = useState("");
  const [msg, setMsg] = useState("");
  const [err, setErr] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!accessToken) {
      setErr("Token de recuperação não encontrado.");
    }
  }, [accessToken]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMsg("");
    setErr("");
    setLoading(true);

    if (senha !== confirma) {
      setErr("As senhas não coincidem.");
      setLoading(false);
      return;
    }
    const { data, error } = await atualizarSenha(accessToken, senha);
    if (error) setErr(error.message);
    else {
      setMsg("Senha atualizada com sucesso!");
      setSenha("");
      setConfirma("");
      setTimeout(() => navigate("/"), 2000);
    }
    setLoading(false);
  };

  return (
    <div className="login-wrapper">
      <div className="login-container">
        <div className="login-box">
          <h2 className="title">Definir Nova Senha</h2>
          <form onSubmit={handleSubmit} className="input-group" autoComplete="off">
            <div className="form-group">
              <label htmlFor="nova-senha" className="input-label">Nova senha</label>
              <input
                id="nova-senha"
                type="password"
                className="input-field"
                placeholder="Digite a nova senha"
                value={senha}
                onChange={(e) => setSenha(e.target.value)}
                required
                minLength={6}
                autoFocus
              />
            </div>
            <div className="form-group">
              <label htmlFor="confirma-senha" className="input-label">Confirme a senha</label>
              <input
                id="confirma-senha"
                type="password"
                className="input-field"
                placeholder="Confirme a nova senha"
                value={confirma}
                onChange={(e) => setConfirma(e.target.value)}
                required
                minLength={6}
              />
            </div>
            <button type="submit" className="login-button" disabled={loading}>
              {loading ? "Atualizando..." : "Atualizar Senha"}
            </button>
          </form>
          {msg && <div className="msg-sucesso">{msg}</div>}
          {err && <div className="msg-erro">{err}</div>}
        </div>
      </div>
    </div>
  );
}
