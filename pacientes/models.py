from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome
    
class Remedio(models.Model):
    remedio = models.CharField(max_length=50)
    quantidade = models.CharField(max_length=50)
    duracao = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.remedio
