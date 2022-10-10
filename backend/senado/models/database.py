from re import L
from unittest.util import _MAX_LENGTH
from django.db import models
import io

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
        tipo = json.keys()[0]
        assunto = Assunto(
            codigo = json[tipo]['Codigo'],
            tipo = tipo,
            descricao = json[tipo]['Descricao']
        )
        assunto.save()
        print(assunto.values())
        return assunto

class Decisao(models.Model):
    data = models.DateTimeField()
    sigla = models.CharField(max_length=200)
    descricao = models.TextField()
    materia = models.ForeignKey('Materia',on_delete=models.DO_NOTHING)

    @staticmethod
    def fromJson(json,materia):
        decisao = Decisao(
            data = json['Data'],
            sigla = json['Sigla'],
            descricao = json['Descricao'],
            materia = materia,
        )
        decisao.save()
        return decisao

class Destino(models.Model):
    sigla = models.CharField(max_length=200)
    descricao = models.TextField()
    materia = models.ForeignKey('Materia',on_delete=models.DO_NOTHING)

    @staticmethod
    def fromJson(json,materia):
        destino = Destino(
            sigla = json['Sigla'],
            descricao = json['Descricao'],
            materia = materia,
        )
        destino.save()
        return destino


class DadosBasicosMateria(models.Model):
    ementaMateria = models.TextField()
    explicacaoEmentaMateria = models.TextField(null=True)
    apelidoMateria = models.TextField(null=True)
    indexacaoMateria = models.ManyToManyField('IndexacaoMateria')
    casaIniciadoraNoLegislativo = models.CharField(max_length=50)
    indicadorComplementar = models.CharField(max_length=50)
    dataApresentacao = models.DateField()
    dataLeitura = models.DateField(null=True)
    siglaCasaLeitura = models.CharField(max_length=50,null=True)
    materia = models.OneToOneField('Materia',on_delete=models.DO_NOTHING)
    NaturezaMateria = models.ForeignKey('NaturezaMateria',on_delete=models.DO_NOTHING)

    @staticmethod
    def fromJson(json,materia):
        natureza = NaturezaMateria.fromJson(json['NaturezaMateria']) if 'NaturezaMateria' in json else None

        dados = DadosBasicosMateria(
            ementaMateria = json['EmentaMateria'],
            explicacaoEmentaMateria = json.get('ExplicacaoEmentaMateria',None),
            apelidoMateria = json.get('ApelidoMateria',None),
            casaIniciadoraNoLegislativo = json['CasaIniciadoraNoLegislativo'],
            indicadorComplementar = json['IndicadorComplementar'],
            dataApresentacao = json['DataApresentacao'],
            dataLeitura = json.get('DataLeitura',None),
            siglaCasaLeitura = json.get('SiglaCasaLeitura',None),
            materia=materia,
            NaturezaMateria = natureza,
        )
        dados.save()
        return dados

class OrigemMateria(models.Model):
    NomePoderOrigem = models.TextField(null=True)
    SiglaCasaOrigem = models.CharField(primary_key=True,max_length=50)

    def fromJson(json):
        origem = OrigemMateria(
            NomePoderOrigem = json.get('NomePoderOrigem',None),
            SiglaCasaOrigem = json['SiglaCasaOrigem'],
        )
        origem.save()
        return origem

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
    autuacao = models.ManyToManyField('Autuacao')
    despacho = models.ManyToManyField('Despacho')
    prazo = models.ManyToManyField('Prazo')
    ordemDoDia = models.ManyToManyField('OrdemDoDia')
    OrigemMateria = models.ForeignKey('OrigemMateria', on_delete=models.DO_NOTHING,null=True)
    MateriaRelacionada = models.ManyToManyField('Materia',related_name='Relacionada')
    MateriaAnexada = models.ManyToManyField('Materia',related_name='Anexada')

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
                OrigemMateria = None,
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

class Autuacao(models.Model):
    NumeroAutuacao = models.BigIntegerField()
    DescricaoAutuacao = models.TextField()
    SituacaoAtual = models.ManyToManyField('SituacaoAtual')
    InformeLegislativo = models.ManyToManyField('InformeLegislativo')

    def fromJson(json):
        autuacao = Autuacao(
            NumeroAutuacao = json['NumeroAutuacao'],
            DescricaoAutuacao = json['DescricaoAutuacao'],
        )
        autuacao.save()
        [autuacao.SituacaoAtual.add(SituacaoAtual.fromJson(x)) for x in json['SituacoesAtuais']['SituacaoAtual']] if 'SituacoesAtuais' in json else None
        [autuacao.InformeLegislativo.add(InformeLegislativo.fromJson(x)) for x in json['InformesLegislativos']['InformeLegislativo']] if 'InformesLegislativos' in json else None
        return autuacao

class SituacaoAtual(models.Model):
    DataSituacao = models.DateField()
    CodigoSituacao = models.BigIntegerField()
    SiglaSituacao = models.CharField(max_length=100)
    DescricaoSituacao = models.TextField()

    def fromJson(json):
        situacao = SituacaoAtual(
            DataSituacao = json['DataSituacao'],
            CodigoSituacao = json['CodigoSituacao'],
            SiglaSituacao = json['SiglaSituacao'],
            DescricaoSituacao = json['DescricaoSituacao'],
        )
        situacao.save()

        return situacao

class SituacaoIniciada(models.Model):
    CodigoSituacao = models.BigIntegerField(primary_key=True)
    SiglaSituacao = models.CharField(max_length=40)

    def fromJson(json):
        situacao = SituacaoIniciada(
            CodigoSituacao = json['CodigoSituacao'],
            SiglaSituacao = json['SiglaSituacao'],
        )
        situacao.save()
        return situacao

class InformeLegislativo(models.Model):
    Data = models.DateTimeField()
    IdInformeLegislativo = models.BigIntegerField(primary_key=True)
    CodigoTramitacaoLegado = models.BigIntegerField(null=True)
    Descricao = models.TextField()
    Local = models.ForeignKey('Local',on_delete=models.DO_NOTHING)
    Colegiado = models.ForeignKey('Colegiado',on_delete=models.DO_NOTHING,null=True)
    SituacaoIniciada = models.ForeignKey('SituacaoIniciada', on_delete=models.DO_NOTHING,null=True)
    TextoAssociado = models.ManyToManyField('TextoAssociado')

    def fromJson(json):
        local = Local.fromJson(json['Local'])
        situacaoIniciada = SituacaoIniciada.fromJson(json['SituacaoIniciada']) if 'SituacaoIniciada' in json else None
        colegiado = Colegiado.fromJson(json['Colegiado']) if 'Colegiado' else None
        informe = InformeLegislativo(
            Data = json['Data'],
            IdInformeLegislativo = json['IdInformeLegislativo'],
            CodigoTramitacaoLegado = json.get('CodigoTramitacaoLegado',None),
            Descricao = json['Descricao'],
            Local = local,
            SituacaoIniciada = situacaoIniciada,
            Colegiado = colegiado,
        )
        informe.save()
        if('TextosAssociados' in json):
            [informe.TextoAssociado.add(TextoAssociado.fromJson(x)) for x in json['TextosAssociados']['TextoAssociado']]
        return informe

class Local(models.Model):
    CodigoLocal = models.BigIntegerField(primary_key=True)
    SiglaLocal = models.CharField(max_length=100)
    NomeLocal = models.TextField()
    SiglaCasaLocal = models.CharField(max_length=50)
    NomeCasaLocal = models.TextField()

    def fromJson(json):
        local = Local(
            CodigoLocal = json['CodigoLocal'],
            SiglaLocal = json['SiglaLocal'],
            NomeLocal = json['NomeLocal'],
            SiglaCasaLocal = json['SiglaCasaLocal'],
            NomeCasaLocal = json['NomeCasaLocal'],
        )
        local.save()
        return local
class Colegiado(models.Model):
    CodigoColegiado = models.BigIntegerField(primary_key=True)
    SiglaColegiado = models.CharField(max_length=50)
    NomeColegiado = models.TextField()
    SiglaCasaColegiado = models.CharField(max_length=50)
    NomeCasaColegiado = models.TextField()

    def fromJson(json):
        colegiado = Colegiado(
            CodigoColegiado = json['CodigoColegiado'],
            SiglaColegiado = json['SiglaColegiado'],
            NomeColegiado = json['NomeColegiado'],
            SiglaCasaColegiado = json['SiglaCasaColegiado'],
            NomeCasaColegiado = json['NomeCasaColegiado'],
        )
        colegiado.save()
        return colegiado

class TextoAssociado(models.Model):
    CodigoTexto = models.BigIntegerField(primary_key=True)
    DescricaoTipoTexto = models.TextField()
    TipoDocumento = models.CharField(max_length=50)
    FormatoTexto = models.CharField(max_length=200)
    DataTexto = models.DateField()
    UrlTexto = models.URLField()
    DescricaoTexto = models.TextField()
    AutoriaTexto = models.TextField()

    def fromJson(json):
        texto = TextoAssociado(
            CodigoTexto = json['CodigoTexto'],
            DescricaoTipoTexto = json['DescricaoTipoTexto'],
            TipoDocumento = json['TipoDocumento'],
            FormatoTexto = json['FormatoTexto'],
            DataTexto = json['DataTexto'],
            UrlTexto = json['UrlTexto'],
            DescricaoTexto = json['DescricaoTexto'],
            AutoriaTexto = json['AutoriaTexto'],
        )
        texto.save()
        return texto
    
class Despacho(models.Model):
    DataDespacho = models.DateField()
    TipoMotivacao = models.TextField()
    IndicadorDespachoCancelado = models.CharField(max_length=50)
    Observacao1Despacho = models.TextField()
    Providencia = models.ManyToManyField('Providencia')

    def fromJson(json):
        despacho = Despacho(
            DataDespacho = json['DataDespacho'],
            TipoMotivacao = json['TipoMotivacao']['TipoMotivacao'],
            IndicadorDespachoCancelado = json['IndicadorDespachoCancelado'],
            Observacao1Despacho = json['Observacao1Despacho'],
        )
        despacho.save()
        [despacho.Providencia.add(Providencia.fromJson(x)) for x in json['Providencias']['Providencia']]
        return despacho

class Providencia(models.Model):
    SiglaTipoProcedimento = models.CharField(max_length=100)
    DescricaoTipoProcedimento = models.TextField()
    NumOrdemProvidencia = models.IntegerField()
    IndicadorReexame = models.CharField(max_length=50)
    Destinatario = models.ManyToManyField('Destinatario')

    def fromJson(json):
        providencia = Providencia(
            SiglaTipoProcedimento = json['SiglaTipoProcedimento'],
            DescricaoTipoProcedimento = json['DescricaoTipoProcedimento'],
            NumOrdemProvidencia = json['NumOrdemProvidencia'],
            IndicadorReexame = json['IndicadorReexame'],
        )
        providencia.save()
        [providencia.Destinatario.add(Destinatario.fromJson(x)) for x in json['Destinatarios']['Destinatario']]
        return providencia

class Destinatario(models.Model):
    NumeroOrdem = models.IntegerField()
    TipoDeliberacao = models.CharField(max_length=100)
    CodigoColegiado = models.CharField(max_length=50)
    SiglaColegiado = models.CharField(max_length=50)
    SiglaCompleta = models.CharField(max_length=50)
    SiglaCasaColegiado = models.CharField(max_length=50)
    NomeColegiado = models.TextField()

    def fromJson(json):
        destinatario = Destinatario(
            NumeroOrdem = json['NumeroOrdem'],
            TipoDeliberacao = json['TipoDeliberacao'],
            CodigoColegiado = json['CodigoColegiado'],
            SiglaColegiado = json['SiglaColegiado'],
            SiglaCompleta = json['SiglaCompleta'],
            SiglaCasaColegiado = json['SiglaCasaColegiado'],
            NomeColegiado = json['NomeColegiado'],
        )
        destinatario.save()
        return destinatario

class Prazo(models.Model):
    CodigoTipoPrazo = models.BigIntegerField(primary_key=True)
    DescricaoTipoPrazo = models.TextField()
    DescricaoTipoFundamento = models.TextField()
    TipoFase = models.CharField(max_length=50)
    DescricaoTipoFase = models.TextField()
    IndicadorProrrogado = models.CharField(max_length=50)
    DataInicioPrazo = models.DateField()
    DataFimPrazo = models.DateField()
    IdentificacaoComissao = models.ForeignKey('IdentificacaoComissao', on_delete=models.DO_NOTHING)

    def fromJson(json):
        comissao = IdentificacaoComissao.fromJson(json['IdentificacaoComissao']) if 'IdentificacaoComissao' in json else None

        prazo = Prazo(
            CodigoTipoPrazo = json['CodigoTipoPrazo'],
            DescricaoTipoPrazo = json['DescricaoTipoPrazo'],
            DescricaoTipoFundamento = json['DescricaoTipoFundamento'],
            TipoFase = json['TipoFase'],
            DescricaoTipoFase = json['DescricaoTipoFase'],
            IndicadorProrrogado = json['IndicadorProrrogado'],
            DataInicioPrazo = json['DataInicioPrazo'],
            DataFimPrazo = json['DataFimPrazo'],
            IdentificacaoComissao = comissao,
        )
        prazo.save()
        return prazo

class IdentificacaoComissao(models.Model):
    CodigoComissao = models.CharField(max_length=50)
    SiglaComissao = models.CharField(max_length=50)
    NomeComissao = models.TextField()
    SiglaCasaComissao = models.CharField(max_length=50)
    NomeCasaComissao = models.TextField()

    def fromJson(json):
        comissao = IdentificacaoComissao(
            CodigoComissao = json['CodigoComissao'],
            SiglaComissao = json['SiglaComissao'],
            NomeComissao = json['NomeComissao'],
            SiglaCasaComissao = json['SiglaCasaComissao'],
            NomeCasaComissao = json['NomeCasaComissao'],
        )
        comissao.save()
        return comissao

class OrdemDoDia(models.Model):
    DataOrdemDoDia = models.DateField()
    DescricaoTipoApreciacao = models.TextField()
    DescricaoResultado = models.TextField()
    SessaoPlenaria = models.ForeignKey('SessaoPlenaria',on_delete=models.DO_NOTHING)

    def fromJson(json):
        sessao = SessaoPlenaria.fromJson(json['SessaoPlenaria']) if 'SessaoPlenaria' in json else None

        ordem = OrdemDoDia(
            DataOrdemDoDia = json['DataOrdemDoDia'],
            DescricaoTipoApreciacao = json['DescricaoTipoApreciacao'],
            DescricaoResultado = json['DescricaoResultado'],
            SessaoPlenaria = sessao,
        )
        ordem.save()
        return ordem

class SessaoPlenaria(models.Model):
    CodigoSessao = models.BigIntegerField()
    SiglaCasaSessao = models.CharField(max_length=50)
    NomeCasaSessao = models.TextField()
    CodigoSessaoLegislativa = models.CharField(max_length=50)
    SiglaTipoSessao = models.CharField(max_length=50)
    NumeroSessao = models.BigIntegerField()
    DataSessao = models.DateField()
    HoraInicioSessao = models.TimeField()

    def fromJson(json):
        sessao = SessaoPlenaria(
            CodigoSessao = json['CodigoSessao'],
            SiglaCasaSessao = json['SiglaCasaSessao'],
            NomeCasaSessao = json['NomeCasaSessao'],
            CodigoSessaoLegislativa = json['CodigoSessaoLegislativa'],
            SiglaTipoSessao = json['SiglaTipoSessao'],
            NumeroSessao = json['NumeroSessao'],
            DataSessao = json['DataSessao'],
            HoraInicioSessao = json['HoraInicioSessao'],
        )
        sessao.save()
        return sessao