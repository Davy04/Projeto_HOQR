from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Paciente, Remedio
import re
from django.core import serializers
import json
# Create your views here.
def pacientes (request):
    if request.method == 'GET':
        pacientes_list = Paciente.objects.all()
        return render(request, 'pacientes.html', {'pacientes': pacientes_list })
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        remedios = request.POST.getlist('remedio')
        quantidades = request.POST.getlist('quantidade')
        duracao = request.POST.getlist('duracao')

        paciente = Paciente.objects.filter(cpf=cpf)

        if paciente.exists():
            return render(request, 'pacientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'remedios': zip(remedios,quantidades,duracao) })
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'pacientes.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'remedios': zip(remedios,quantidades,duracao)})

        paciente = Paciente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )

        paciente.save()

        for remedio, quantidade, duracao in zip(remedios,quantidades,duracao):
            pac = Remedio(remedio=remedio, quantidade=quantidade, duracao=duracao, paciente=paciente)
            pac.save()

        return HttpResponse('teste')   

def att_paciente(request):
    id_paciente = request.POST.get('id_paciente') 

    paciente = Paciente.objects.filter(id=id_paciente)
    remedios = Remedio.objects.filter(paciente=paciente[0])

    paciente_json = json.loads( serializers.serialize('json', paciente))[0]['fields']
    remedios_json = json.loads( serializers.serialize('json', remedios))
    remedios_json = [{'fields': remedio['fields'], 'id': remedio['pk']} for remedio in remedios_json]
    print(remedios_json)
    return JsonResponse(paciente_json)