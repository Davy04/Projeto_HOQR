from django.shortcuts import render
from django.http import HttpResponse
from .models import Paciente, Remedio
import re
# Create your views here.
def pacientes (request):
    if request.method == 'GET':
        return render(request, 'pacientes.html')
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