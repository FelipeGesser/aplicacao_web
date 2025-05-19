import { supabase } from "../supabase";

/**
 * Atualiza a senha do usuário usando o token de recuperação.
 * @param {string} accessToken - Token de recuperação recebido por e-mail.
 * @param {string} newPassword - Nova senha.
 * @returns {{ data: object|null; error: { message: string }|null }}
 */
export async function atualizarSenha(accessToken, newPassword) {
  // Define sessão temporária com o access_token
  await supabase.auth.setSession({
    access_token: accessToken,
    refresh_token: "",
  });

  const { data, error } = await supabase.auth.updateUser({
    password: newPassword,
  });

  return { data, error };
}
