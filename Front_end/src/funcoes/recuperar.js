import { supabase } from "../supabase";

/**
 * Envia e-mail com link de redefinição de senha.
 * @param {string} email - E-mail do usuário.
 * @returns {{ data: object|null; error: { message: string }|null }}
 */
export async function recuperarSenha(email) {
  const redirectTo = window.location.origin + "/atualizasenha";
  const { data, error } = await supabase.auth.resetPasswordForEmail(email, {
    redirectTo,
  });
  return { data, error };
}
