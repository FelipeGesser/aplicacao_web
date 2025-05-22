from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase_client import cadastro_usuario, login_usuario
from supabase import create_client
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/mensagem')
def mensagem():
    return jsonify({'mensagem': 'Olá do backend em Python!'})

@app.route('/api/atualizar-senha', methods=['POST'])
def atualizar_senha():
    data = request.json
    access_token = data.get('access_token')
    new_password = data.get('new_password')
    if not access_token or not new_password:
        return jsonify({'error': 'Token e nova senha são obrigatórios.'}), 400
    try:
        # Cria um client autenticado temporário
        from supabase import ClientOptions
        SUPABASE_URL = os.getenv("SUPABASE_URL")
        SUPABASE_KEY = os.getenv("SUPABASE_KEY")
        options = ClientOptions(headers={"Authorization": f"Bearer {access_token}"})
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY, options)
        res = supabase.auth.update_user({"password": new_password})
        if res.user:
            return jsonify({'success': True, 'user': res.user.id})
        return jsonify({'success': False, 'error': str(res)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
