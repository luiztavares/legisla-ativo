from django.db import models

# Create your models here.

class Materia(models.Model):
    codigo = models.BigIntegerField()
    identificacao_processo = models.BigIntegerField(primary_key=True)
    descricao_identificacao = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    numero = models.CharField(max_length=20)
    ano = models.CharField(max_length=4)
    ementa = models.TextField(null=True)
    autor = models.CharField(max_length=100)
    data = models.DateField()
    url_detalhe_materia = models.URLField()

    @classmethod
    def from_json(cls, json):
        materia = cls(
            codigo = json['Codigo'],
            identificacao_processo = json['IdentificacaoProcesso'],
            descricao_identificacao = json['DescricaoIdentificacao'],
            sigla = json['Sigla'],
            numero = json['Numero'],
            ano = json['Ano'],
            ementa = json.get('Ementa',None),
            autor = json['Autor'],
            data = json['Data'],
            url_detalhe_materia = json['UrlDetalheMateria'],
        )
        return materia
    
    def __str__(self):
        return self.descricao_identificacao



class Parlamentar(models.Model):
    codigoParlamentar = models.BigIntegerField(primary_key=True)
    codigoPublicoNaLegAtual = models.BigIntegerField(null=True)
    codigoDeputadoNaCamara = models.BigIntegerField(null=True)
    nomeParlamentar = models.CharField(max_length=100)
    nomeCompletoParlamentar = models.CharField(max_length=100)
    sexoParlamentar = models.CharField(max_length=100)
    formaTratamento = models.CharField(max_length=100)
    emailParlamentar = models.EmailField(null=True)
    siglaPartidoParlamentar = models.CharField(null=True,max_length=100)
    ufParlamentar = models.CharField(null=True,max_length=100)

    @classmethod
    def fromJson(cls,json):
        parlamentar = cls(
            codigoParlamentar = json['CodigoParlamentar'],
            codigoPublicoNaLegAtual = json.get('CodigoPublicoNaLegAtual',None),
            codigoDeputadoNaCamara = json.get('CodigoDeputadoNaCamara',None),
            nomeParlamentar = json['NomeParlamentar'],
            nomeCompletoParlamentar = json['NomeCompletoParlamentar'],
            sexoParlamentar = json['SexoParlamentar'],
            formaTratamento = json['FormaTratamento'],
            emailParlamentar = json.get('EmailParlamentar',None),
            siglaPartidoParlamentar = json.get('SiglaPartidoParlamentar',None),
            ufParlamentar = json.get('UfParlamentar',None),
        )
        return parlamentar

class Iniciativa(models.Model):
    siglaTipoIniciativa = models.CharField(max_length=100)
    descricaoTipoIniciativa = models.CharField(max_length=100)
    descricaoIniciativa = models.CharField(max_length=100)
    identificacaoParlamentar = models.ForeignKey(Parlamentar,on_delete=models.PROTECT,null=True)
    materia = models.ManyToManyField(Materia)

    @classmethod
    def fromJson(cls,json):
        parlamentar = None
        if ('IdentificacaoParlamentar' in json):
            parlamentar = Parlamentar.fromJson(json['IdentificacaoParlamentar'])
            parlamentar.save()

        iniciativa = cls(
            siglaTipoIniciativa = json['SiglaTipoIniciativa'],
            descricaoTipoIniciativa = json['DescricaoTipoIniciativa'],
            descricaoIniciativa = json['DescricaoIniciativa'],
            identificacaoParlamentar = parlamentar,
        )

        return iniciativa

class Autoria(models.Model):
    nomeAutor = models.CharField(max_length=100)
    siglaTipoAutor = models.CharField(max_length=100)
    descricaoTipoAutor = models.CharField(max_length=100)
    numOrdemAutor = models.IntegerField()
    identificacaoParlamentar = models.ForeignKey(Parlamentar,on_delete=models.PROTECT,null=True)
    materia = models.ManyToManyField(Materia)

    @classmethod
    def fromJson(cls,json):
        parlamentar = None
        if ('IdentificacaoParlamentar' in json):
            parlamentar = Parlamentar.fromJson(json['IdentificacaoParlamentar'])
            parlamentar.save()
        autor = cls(
            nomeAutor = json['NomeAutor'],
            siglaTipoAutor = json['SiglaTipoAutor'],
            descricaoTipoAutor = json['DescricaoTipoAutor'],
            numOrdemAutor = json['NumOrdemAutor'],
            identificacaoParlamentar = parlamentar,

        )
        return autor