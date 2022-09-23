from re import L
from django.db import models

class NaturezaMateria(models.Model):
    codigoNatureza = models.BigIntegerField(primary_key=True)
    nomeNatureza = models.CharField(max_length=100)
    descricaoNatureza = models.CharField(max_length=200)

    @staticmethod
    def fromJson(json):
        natureza = NaturezaMateria(
            codigoNatureza = json['CodigoNatureza'],
            nomeNatureza = json['NomeNatureza'],
            descricaoNatureza = json['DescricaoNatureza'],
        )
        natureza.save()
        return natureza

class IndexacaoMateria(models.Model):
    index = models.CharField(max_length=200,primary_key=True)

class Classificacao(models.Model):
    codigoClasse = models.BigIntegerField(primary_key=True)
    descricaoClasse = models.CharField(max_length=200)
    descricaoClasseHierarquica = models.CharField(max_length=200)

    @staticmethod
    def fromJson(json):
        classificacao = Classificacao(
            codigoClasse = json['CodigoClasse'],
            descricaoClasse = json['DescricaoClasse'],
            descricaoClasseHierarquica = json['DescricaoClasseHierarquica']
        )
        classificacao.save()
        return classificacao

class Assunto(models.Model):
    codigo = models.BigIntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)

    @staticmethod
    def fromJson(json):
        assunto = Assunto(
            codigo = json['Codigo'],
            tipo = json['Tipo'],
            descricao = json['Descricao']
        )

class Decisao(models.Model):
    data = models.DateTimeField()
    sigla = models.CharField(max_length=200)
    descricao = models.TextField()
    materia = models.ForeignKey('Materia',on_delete=models.DO_NOTHING)

    @staticmethod
    def fromJson(json):
        decisao = Decisao(
            data = json['Data'],
            sigla = json['Sigla'],
            descricao = json['Descricao'],
            materia = json['Materia'],
        )
        decisao.save()
        return decisao

class Destino(models.Model):
    sigla = models.CharField(max_length=200)
    descricao = models.TextField()
    materia = models.ForeignKey('Materia',on_delete=models.DO_NOTHING)

    @staticmethod
    def fromJson(json):
        destino = Destino(
            sigla = json['Sigla'],
            descricao = json['Descricao'],
            materia = json['Materia'],
        )
        destino.save()
        return destino


class DadosBasicosMateria(models.Model):
    ementaMateria = models.TextField()
    explicacaoEmentaMateria = models.TextField()
    apelidoMateria = models.TextField()
    indexacaoMateria = models.ManyToManyField('IndexacaoMateria')
    casaIniciadoraNoLegislativo = models.CharField(max_length=50)
    indicadorComplementar = models.CharField(max_length=50)
    dataApresentacao = models.DateField()
    dataLeitura = models.DateField
    siglaCasaLeitura = models.CharField(max_length=50)
    materia = models.ForeignKey('Materia',on_delete=models.DO_NOTHING)
    natureza = models.ForeignKey('NaturezaMateria',on_delete=models.DO_NOTHING)

    @staticmethod
    def fromJson(json):
        print(json)
        natureza = NaturezaMateria.fromJson(json['NaturezaMateria'])
        natureza.save()
        dados = DadosBasicosMateria(
            EmentaMateria = json['EmentaMateria'],
            explicacaoEmentaMateria = json['ExplicacaoEmentaMateria'],
            apelidoMateria = json['ApelidoMateria'],
            casaIniciadorNoLegislativo = json['CasaIniciadorNoLegislativo'],
            indicadorComplementar = json['IndicadorComplementar'],
            dataApresentacao = json['DataApresentacao'],
            dataLeitura = json['DataLeitura'],
            siglaCasaLeitura = json['SiglaCasaLeitura'],
            natureza = natureza,
        )
        dados.save()
        return dados

class Materia(models.Model):
    codigo = models.CharField(max_length=20,primary_key=True)
    identificacaoProcesso = models.CharField(max_length=20,null=True)
    descricaoIdentificacao = models.CharField(max_length=100,null=True)
    sigla = models.CharField(max_length=10,null=True)
    numero = models.CharField(max_length=10,null=True)
    ano = models.CharField(max_length=4,null=True)
    siglaComissao = models.CharField(max_length=20,null=True)
    ementa = models.TextField(null=True)
    autor = models.TextField(null=True)
    data = models.DateField(null=True)
    urlDetalheMateria = models.URLField(null=True)
    classificacao = models.ManyToManyField(Classificacao)
    assunto = models.ManyToManyField(Assunto)
    autoria = models.ManyToManyField('Autoria')
    emenda = models.ManyToManyField('Emenda')

    @staticmethod
    def fromJson(json):
        materia = Materia(
                codigo = json['Codigo'],
                identificacaoProcesso = json['IdentificacaoProcesso'],
                descricaoIdentificacao = json['DescricaoIdentificacao'],
                sigla = json['Sigla'],
                numero = json['Numero'],
                ano = json['Ano'],
                siglaComissao = json.get('SiglaComissao',None),
                ementa = json.get('Ementa',None),
                autor = json['Autor'],
                data = json['Data'],
                urlDetalheMateria = json['UrlDetalheMateria'],
            )
        materia.save()
        return materia

class Autoria(models.Model):
    nomeAutor = models.TextField(primary_key=True)
    siglaTipoAutor = models.CharField(max_length=200)
    descricaoTipoAutor = models.CharField(max_length=200)
    numOrdemAutor = models.IntegerField()

    @staticmethod
    def fromJson(json):
        autoria = Autoria(
            nomeAutor = json['NomeAutor'],
            siglaTipoAutor = json['SiglaTipoAutor'],
            descricaoTipoAutor = json['DescricaoTipoAutor'],
            numOrdemAutor = json['NumOrdemAutor'],
        )
        autoria.save()
        if('IdentificacaoParlamentar' in json):
            parlamentar = Parlamentar.fromJson(json['IdentificacaoParlamentar'])
            parlamentar.save()
            parlamentar.autoria.add(autoria)
        return autoria


class Parlamentar(models.Model):
    codigoParlamentar = models.BigIntegerField(primary_key=True)
    nomeParlamentar = models.TextField()
    nomeCompletoParlamentar = models.TextField()
    sexoParlamentar = models.CharField(max_length=20)
    formaTratamento = models.CharField(max_length=50,null=True)
    urlFotoParlamentar = models.URLField(null=True)
    urlPaginaParlamentar = models.URLField(null=True)
    emailParlamentar = models.EmailField(null=True)
    siglaPartidoParlamentar = models.CharField(max_length=100,null=True)
    ufParlamentar = models.CharField(max_length=10,null=True)
    autoria = models.ManyToManyField('Autoria')

    @staticmethod
    def fromJson(json):
        parlamentar = Parlamentar(
                codigoParlamentar = json['CodigoParlamentar'],
                nomeParlamentar =json['NomeParlamentar'],
                nomeCompletoParlamentar = json['NomeCompletoParlamentar'],
                sexoParlamentar = json['SexoParlamentar'],
                formaTratamento = json.get('FormaTratamento',None),
                urlFotoParlamentar = json.get('UrlFotoParlamentar',None),
                urlPaginaParlamentar = json.get('UrlPaginaParlamentar',None),
                emailParlamentar = json.get('EmailParlamentar',None),
                siglaPartidoParlamentar = json.get('SiglaPartidoParlamentar',None),
                ufParlamentar = json.get('UfParlamentar',None),
        )
        return parlamentar
        

class Emenda(models.Model):
    codigoEmenda = models.BigIntegerField(primary_key=True)
    numeroEmenda = models.CharField(max_length=20)
    dataApresentacao = models.DateField()
    colegiadoApresentacao = models.CharField(max_length=20)
    descricaoTurno = models.CharField(max_length=100)
    descricaoTipoEmenda = models.CharField(max_length=200)

    @staticmethod
    def fromJson(json):
        emenda = Emenda(
            codigoEmenda = json['CodigoEmenda'],
            numeroEmenda = json['NumeroEmenda'],
            dataApresentacao = json['DataApresentacao'],
            colegiadoApresentacao = json['ColegiadoApresentacao'],
            descricaoTurno = json['DescricaoTurno'],
            descricaoTipoEmenda = json['DescricaoTipoEmenda'],
        )
        emenda.save()
        return emenda
