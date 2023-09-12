from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    # Outros campos relevantes para os médicos

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    # Outros campos relevantes para os prontuários

class Administrador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
