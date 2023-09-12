from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def pagina_funcionario(request):
    # Lógica da página de funcionários
    return render(request, 'autenticacao_qr/funcionario_page.html')

@login_required
def pagina_paciente(request):
    # Lógica da página de pacientes
    return render(request, 'autenticacao_qr/paciente_page.html')

@login_required
def pagina_administrador(request):
    # Lógica da página de administradores
    return render(request, 'autenticacao_qr/administrador_page.html')
