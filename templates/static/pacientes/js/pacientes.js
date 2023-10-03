function add_remedio(){
    container = document.getElementById('form-remedio')

    html = "<br>  <div class='row'> <div class='col-md'> <input type='text' placeholder='remedio' class='form-control' name='remedio' > </div> <div class='col-md'><input type='text' placeholder='quantidade' class='form-control' name='quantidade' ></div> <div class='col-md'> <input type='text' placeholder='duração' class='form-control' name='duracao'> </div> </div>"

    container.innerHTML += html
}

function exibir_form(tipo){

    add_paciente = document.getElementById('adicionar-paciente')
    att_paciente = document.getElementById('att_paciente')

    if(tipo == "1"){
        att_paciente.style.display = "none"
        add_paciente.style.display = "block"

    }else if(tipo == "2"){
        add_paciente.style.display = "none";
        att_paciente.style.display = "block"
    }

}


function dados_paciente(){
    paciente = document.getElementById('paciente-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_paciente = paciente.value

    data = new FormData()
    data.append('id_paciente', id_paciente)

    fetch("/pacientes/atualiza_paciente/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data

    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('form-att-paciente').style.display='block'
        
        nome = document.getElementById('nome')
        nome.value = data['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['sobrenome']

        email = document.getElementById('email')
        email.value = data['email']
         
        cpf = document.getElementById('cpf')
        cpf.value = data['cpf']
    })


}


function update_paciente(){
    nome = document.getElementById('nome').value
    sobrenome = document.getElementById('sobrenome').value
    email = document.getElementById('email').value
    cpf = document.getElementById('cpf').value
    id = document.getElementById('id').value

    fetch('/pacientes/update_paciente/' + id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            sobrenome: sobrenome,
            email: email,
            cpf: cpf,
        })

    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        if(data['status'] == '200'){
            nome = data['nome']
            sobrenome = data['sobrenome']
            email = data['email']
            cpf = data['cpf']
            console.log('Dados alterado com sucesso')
        }else{
            console.log('Ocorreu algum erro')
        }
    })

}