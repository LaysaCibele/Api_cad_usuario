# Api_cad_usuário

Sistema de Cadastro de Usuários  
API REST para cadastro e gerenciamento de usuários, construída com Flask e SQLite.


 Tecnologias
- Python 3.12
- Flask
- SQLite
- HTML + CSS (para os templates)


Passo a passo para rodar o projeto (localmente): 
  
  1. Clone o repositório
     ```bash
     git clone https://github.com/LaysaCibele/Api_cad_usuario.git
     cd cad_usuario (ou o nome que você der para a pasta.)

  2. Crie um ambiente virtual
     ```bash
     python -m venv venv
     .\venv\Scripts\activate #Windows

  3.Instale as dependências
       ```bash
       
         pip install -r requeriments.txt

 4. Execute a aplicação
    ```bash
      python app.py
A aplicação estará disponível em: http://localhost:5000

 5. Como consultar as informações dos usuários cadastrados?
    ```bash
    sqlite3 users.db
    SELECT id, nome, email, cpf FROM users;

Postman: 
New --> http --> Selecione o método do tipo POST e cole a URL disponibilizada ao rodar o ('python app.py') --> Body (selecione "raw" e text do tipo JSON) --> Send.

   Laysa Cibele - Estudante do 2° período de Ciência da Computação
   [GitHub: https://github.com/LaysaCibele] 

