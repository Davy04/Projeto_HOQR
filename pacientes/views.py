from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pacientes (request):
    return render(request, 'pacientes.html')
