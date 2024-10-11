from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()

class Usuario(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.nome
