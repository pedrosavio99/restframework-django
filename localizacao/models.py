from django.db import models

# Create your models here.
class Localizacao(models.Model):
    #olhe, aqui vc po0de perceber que nçao foi adicionado a ru e endereço pra poder
    #abranger mais situações
    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    pais = models.CharField(max_length=70)

    def __str__(self):
        return self.linha1


