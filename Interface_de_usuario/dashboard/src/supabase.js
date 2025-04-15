import { createClient } from "@supabase/supabase-js";

const supabaseUrl = "https://vbyzgdczkvddiypikkbz.supabase.co";
const supabaseKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZieXpnZGN6a3ZkZGl5cGlra2J6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ1NzQwMjIsImV4cCI6MjA2MDE1MDAyMn0.1fI1aO1v8ebqJX4v5fhPACsvNE0yy0xuEAiAhQ4W6k4";

export const supabase = createClient(supabaseUrl, supabaseKey);
