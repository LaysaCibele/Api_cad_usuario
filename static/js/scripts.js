//Nova etapa: Aqui que vai acontecer a troca entre cadastro e login

function mostrarLogin(){
    document.getElementById('form-cadastro').style.display = "none";
    document.getElementById('form-login').style.display = "block";
}


function mostrarCadastro(){
    document.getElementById('form-login').style.display = "none";
    document.getElementById('form-cadastro').style.display = "block";
}

//Meu JS de cadastro (antes do login)
const form = document.getElementById('cadForm');

form.addEventListener('submit', async(evento) => {
    evento.preventDefault();


    const dados = {
        nome: document.getElementById('nome').value,
        email: document.getElementById('email').value,
        cpf: document.getElementById('cpf').value,
        senha: document.getElementById('senha').value
    };

    const resposta = await fetch('/api/users', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(dados) //Aqui eu converto o objeto JS em JSON
    });

    const resultado = await resposta.json();

    if (resposta.ok){
        alert('Usuário cadastrado com sucesso!');
        form.reset();
    }
    else{
        alert('ERRO. Falha no cadastro.')
    }
});

//Nova etapa do JS (Agora temos o login)

const loginForm = document.getElementById('loginForm');

loginForm.addEventListener('submit', async(evento) => {
    evento.preventDefault();

    const dadosLogin = {
        email: document.getElementById('loginEmail').value,
        senha: document.getElementById('loginSenha').value
    };

        const resposta = await fetch('/api/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(dadosLogin) //Aqui eu converto o objeto JS em JSON
    });

    const data = await resposta.json();

    if (resposta.ok){
        alert("Login realizado!")
        form.reset();
    }
    else{
        alert("data.erro");
    }
});