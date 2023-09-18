from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pacientes (request):
    if request.method == 'GET':
        return render(request, 'pacientes.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')


        print(carros)
        return HttpResponse('teste')