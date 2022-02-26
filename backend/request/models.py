from django.db import models
from request.request import Request

# Create your models here.
class MateriaPesquisaLista(models.Model,Request):
    url = 'https://legis.senado.leg.br/dadosabertos/materia/pesquisa/lista?'
    class Boleana(models.TextChoices):
        S = 'S', "Sim"
        N = 'N', "Não"

    ano = models.CharField(max_length=4)
    anoNorma = models.CharField(max_length=4)
    codigoClasse = models.BigIntegerField()
    codigoConteudo = models.BigIntegerField()
    dataFimApresentacao = models.CharField(max_length=8)
    dataInicioApresentacao = models.CharField(max_length=8)
    nomeAutor = models.TextField()
    numero = models.BigIntegerField()
    numeroNorma = models.BigIntegerField()
    palavraChave = models.TextField()
    sigla = models.CharField(max_length=50)
    siglaComissaoReq = models.CharField(max_length=50)
    tipoNorma = models.CharField(max_length=50)
    tramitando = models.CharField(max_length=1,choices=Boleana.choices)
    v = models.CharField(max_length=10)

class AutoriaRequest(models.Model,Request):
    codigo = models.BigIntegerField(primary_key=True)

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/autoria/{self.codigo}'
