import sqlite3
from pathlib import path


#Variável global constante - guarda o caminho do arquivo do db de dados sqlite
DB_PATH = Path('users.db')


def init_db():
    conn = sqlite3.connect(DB_PATH) #Abri uma conexão com o banco de dados
    cur = conn.cursor() #Criei um cursor que é o objeto que vai executar os comandos do SQL
    
    
#Criando a minha tabela (users)
# comando SQL que eu passei como uma string multilinha para o método cur.execute() - 

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 
            """)

conn.commit() #gravando as mudançassss
conn.close() #fechando a conexão com o banco :)


if __name__ == '__main__':
    init_db()
    print(f"Banco de dados inicializado em {DB_PATH}")
    