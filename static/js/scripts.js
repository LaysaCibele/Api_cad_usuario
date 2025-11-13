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
})