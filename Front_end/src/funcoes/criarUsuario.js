import { supabase } from "../supabase";

export async function registrarUsuario(email, senha) {
  const { data, error } = await supabase.auth.signUp({
    email,
    password: senha,
  });

  return { data, error };
}
