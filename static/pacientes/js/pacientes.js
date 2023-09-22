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
        document.getElementById('form-att-paciente').style.display = 'block'
        
        id = document.getElementById('id')
        id.value = data['paciente_id']

        nome = document.getElementById('nome')
        nome.value = data['paciente']['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['paciente']['sobrenome']

        cpf = document.getElementById('cpf')
        cpf.value = data['paciente']['cpf']

        email = document.getElementById('email')
        email.value = data['paciente']['email']

        div_remedios = document.getElementById('remedios')

        for(i=0; i<data['remedios'].length; i++){
            div_remedios.innerHTML += "\<form action='/pacientes/update_remedio/" + data['remedios'][i]['id'] +"' method='POST'>\
                <div class='row'>\
                        <div class='col-md'>\
                            <input class='form-control' name='remedio' type='text' value='" + data['remedios'][i]['fields']['remedio'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' name='quantidade' type='text' value='" + data['remedios'][i]['fields']['quantidade'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' type='text' name='duracao' value='" + data['remedios'][i]['fields']['duracao'] + "' >\
                        </div>\
                        <div class='col-md'>\
                            <input class='btn btn-lg btn-success' type='submit'>\
                        </div>\
                    </form>\
                    <div class='col-md'>\
                        <a href='/pacientes/excluir_remedio/"+ data['remedios'][i]['id'] +"' class='btn btn-lg btn-danger'>EXCLUIR</a>\
                    </div>\
                </div><br>"
        }
        
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