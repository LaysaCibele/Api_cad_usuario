from flask import Flask, request, render_template,  redirect, url_for, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS # Permite que meu front chame minha API
from pathlib import Path #manipulação de caminhos


DB_PATH = Path('users.db')
#Abaixo, eu criei um apalicação Web 
app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app) #Vai permitir que o formulário envie dados ao flask 


def get_db_conncetion():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('cadastro.html')  #aqui eu tô carregando o arquivo html do formulário


@app.route('/submit', methods=['POST'])
def submit_form():
    nome = request.form.get('nome')
    email = request.form.get('email') 
    cpf = request.form.get('cpf') 
    senha = request.form.get('senha')
    
    
    if not nome or not email or not cpf or not senha:
        return "Dados incompletos", 400


    senha_hash = generate_password_hash(senha)
    
    conn = get_db_conncetion()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (nome, email, cpf, senha_hash) VALUES (?, ?, ?, ?)",
            (nome, email, cpf, senha_hash)
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        conn.rollback() #desfaz a transação se houver erro
        return f"Erro de integridade: {e}", 400
    finally:
        conn.close()
        
    return redirect(url_for('index'))

#Abaixo, cheguei na etapa de criar usuário via JSON 
@app.route('/api/users', methods=['POST'])

def api_criar_usuario():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    cpf = data.get('cpf')
    senha = data.get('senha')
    
    if not nome or not email or not cpf or not senha:
        return jsonify({"erro": "Faltam dados obrigatórios."}), 400
    
    
    senha_hash = generate_password_hash(senha)
    conn = get_db_conncetion()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (nome, email, cpf, senha_hash) VALUES (?, ?, ?, ?)",
            (nome, email, cpf, senha_hash)
        )
        conn.commit()
        user_id = cur.lastrowid  # pega o ID gerado automaticamente
    except sqlite3.IntegrityError as e:
        conn.rollback()
        return jsonify({"erro": f"Erro ao cadastrar usuário: {str(e)}"}), 400
    finally:
        conn.close()

    return jsonify({"id": user_id, "nome": nome, "email": email}), 201


@app.route('/api/users/<int:user_id>', methods=['GET'])
def api_get_usuario(user_id):
    ...
    
       
if __name__ == '__main__':
    app.run(debug=True)
