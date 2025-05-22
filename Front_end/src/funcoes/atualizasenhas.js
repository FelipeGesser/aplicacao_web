import { supabase } from "../supabase";

/**
 * Atualiza a senha do usuário usando o token de recuperação via API Flask.
 * @param {string} accessToken - Token de recuperação recebido por e-mail.
 * @param {string} newPassword - Nova senha.
 * @returns {{ data: object|null; error: { message: string }|null }}
 */
export async function atualizarSenha(accessToken, newPassword) {
  try {
    const resp = await fetch("http://localhost:5000/api/atualizar-senha", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ access_token: accessToken, new_password: newPassword })
    });
    const result = await resp.json();
    if (!resp.ok || result.error) {
      return { data: null, error: { message: result.error || "Erro ao atualizar senha" } };
    }
    return { data: result, error: null };
  } catch (err) {
    return { data: null, error: { message: err.message || "Erro de conexão" } };
  }
}
