from django.db import models
from core.tools import Request

class PesquisaMateriaService(models.Model,Request):
    "Pesquisa básica de matérias (busca as matérias que satisfazem aos parâmetros informados). Atenção: 1) Se não informar o ano (da matéria ou da norma) nem o período de apresentação, será considerado o ano atual. 2) Para a pesquisa por período de apresentação, o limite é de 1 ano."
    
    url = 'https://legis.senado.leg.br/dadosabertos/materia/pesquisa/lista?'
    class Boleana(models.TextChoices):
        S = 'S', "Sim"
        N = 'N', "Não"

    ano = models.CharField(max_length=4)  # (opcional) ano da matéria
    anoNorma = models.CharField(max_length=4) # (opcional) ano da norma jurídica gerada
    codigoClasse = models.BigIntegerField() # (opcional) código da classificação da matéria
    codigoConteudo = models.BigIntegerField() # (opcional) código do conteúdo informacional da matéria
    dataFimApresentacao = models.CharField(max_length=8) # (opcional) data de fim para pesquisa da data de apresentação da matéria, no formato AAAAMMDD
    dataInicioApresentacao = models.CharField(max_length=8) # (opcional) data de início para pesquisa da data de apresentação da matéria, no formato AAAAMMDD
    nomeAutor = models.TextField() # (opcional) nome do autor da matéria
    numero = models.BigIntegerField() # (opcional) número da matéria
    numeroNorma = models.BigIntegerField() # (opcional) número da norma jurídica gerada
    palavraChave = models.TextField() # palavra (opcional) chave para a pesquisa
    sigla = models.CharField(max_length=50) # (opcional) sigla da matéria
    siglaComissaoReq = models.CharField(max_length=50) # (opcional) sigla da comissão do requerimento - para requerimentos de comissão a partir de 2019
    tipoNorma = models.CharField(max_length=50) # (opcional) sigla do tipo da norma jurídica gerada
    tramitando = models.CharField(max_length=1,choices=Boleana.choices) # (opcional) indica se retorna apenas as matérias que estão tramitando ("S") ou não ("N")
    v = models.CharField(max_length=10) # (opcional) versão do serviço

class MateriaAutoria(models.Model,Request):
    'Obtém a autoria de uma matéria'

    codigo = models.BigIntegerField(primary_key=True) # Código (ID) da matéria. Identificador único da matéria.
    v = models.IntegerField() # (opcional) - Versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/autoria/{self.codigo}'

class MateriaAtualizacoes(models.Model,Request):
    'Obtém as atualizações mais recentes em uma matéria'

    codigo = models.BigIntegerField() # Código da matéria no banco de dados
    numdias = models.BigIntegerField(default=30) # Número de dias a considerar (X): atualizações ocorridas nos últimos X dias - X por default é 30. Estão disponíbeis as atualizações dos últimos 30 dias.
    v = models.IntegerField() # (opcional) - Versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/atualizacoes/{self.codigo}'

class MateriaEmendas(models.Model,Request):
    'Obtém as emendas de uma matéria'

    codigo = models.BigIntegerField(primary_key=True) # Código (ID) da matéria. Identificador único da matéria.
    v = models.IntegerField() # (opcional) - Versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/emendas/{self.codigo}'

class MateriaRelatorias(models.Model,Request):
    'Obtém as relatorias de uma matéria'

    codigo = models.BigIntegerField(primary_key=True) # Código (ID) da matéria. Identificador único da matéria.
    v = models.IntegerField() # (opcional) - Versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/relatorias/{self.codigo}'

class MateriaTextos(models.Model,Request):
    'Obtém os textos integrais e a legislação citada de uma matéria'

    codigo = models.BigIntegerField(primary_key=True) # Código (ID) da matéria. Identificador único da matéria.
    v = models.IntegerField() # (opcional) - Versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/textos/{self.codigo}'