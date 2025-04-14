Como Rodar o Projeto MyDashboard

1. Instalar o Python

Baixe e instale o Python 3.10 ou superior:
https://www.python.org/downloads/

Na instalação → Marque:  
`Add Python to PATH`

2. Instalar as Bibliotecas Necessárias

Dentro da pasta do projeto:

bash
pip install -r requirements.txt

3. Criar Conta no Supabase

Acesse:
https://supabase.com/

Crie um projeto gratuito

Vá em → Configurações → API

Copie:

SUPABASE_URL
SUPABASE_KEY (anon public)

4. Criar o arquivo .env

SUPABASE_URL=https://SEU_PROJETO.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

(substitua com os dados reais do Supabase)

5. Rodar o Projeto

Dentro da pasta do projeto:

bash
streamlit run dashboard_app.py