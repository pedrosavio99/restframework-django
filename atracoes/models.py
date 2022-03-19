from django.db import models

# Create your models here.
class Atracao(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.TextField()
    horario_fun = models.TextField()
    idade_minima = models.IntegerField()

    def __str__(self):
        return self.nome