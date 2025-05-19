from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/mensagem')
def mensagem():
    return jsonify({'mensagem': 'Olá do backend em Python!'})

if __name__ == '__main__':
    app.run(debug=True)
