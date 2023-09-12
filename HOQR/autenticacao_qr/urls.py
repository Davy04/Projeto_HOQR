from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('funcionario/', views.pagina_funcionario, name='pagina_funcionario'),
    path('paciente/', views.pagina_paciente, name='pagina_paciente'),
    path('administrador/', views.pagina_administrador, name='pagina_administrador'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Outras URLs do seu aplicativo
]
