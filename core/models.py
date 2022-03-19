from django.db import models
from atracoes.models import Atracao  #aqui vamos uyma lista many to many
from comentarios.models import Comentario #essa importacoes são para desenvolver modeos acoplados
from avaliacoes.models import Avaliacao
from localizacao.models import Localizacao
# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.nome
