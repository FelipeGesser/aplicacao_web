import { supabase } from "../supabase";

export async function loginUsuario(email, senha) {
  const { data, error } = await supabase.auth.signInWithPassword({
    email,
    password: senha,
  });

  return { data, error };
}
