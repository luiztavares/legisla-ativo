from .models.api import *
from .models.database import *

from datetime import date
from dateutil.relativedelta import relativedelta

def atualizaTodasAsMaterias():
    try:
        dataInicioApresentacao = Materia.objects.latest('data').data
    except:
        dataInicioApresentacao = date(2020,1,1)
        print('except')
    dataFimApresentacao = dataInicioApresentacao + relativedelta(years=1) - relativedelta(days=1)

    while(dataInicioApresentacao < date.today()):
        request = PesquisaMateriaService(
            dataInicioApresentacao=dataInicioApresentacao.strftime('%Y%m%d'),
            dataFimApresentacao=dataFimApresentacao.strftime('%Y%m%d'),
         )
        request.unpack()
        
        print(dataInicioApresentacao,dataFimApresentacao,len(request.body))

        for json in request.body:
            Materia.fromJson(json)

        dataInicioApresentacao = dataInicioApresentacao + relativedelta(years=1)
        dataFimApresentacao = dataInicioApresentacao + relativedelta(years=1) - relativedelta(days=1)

def atualizaTodosAutores():
    materias = Materia.objects.filter(autoria=None)
    for i,materia in enumerate(materias):
        print(f'{i} of {len(materias)}')
        request = MateriaAutoria(codigo=materia.codigo)
        request.unpack()
        for json in request.body:
            autoria = Autoria.fromJson(json)
            materia.autoria.add(autoria)


def atualizaDetalhes():
    materias = Materia.objects.filter(dadosbasicosmateria__isnull=True).order_by('-data')
    for materia in materias:
        print(materia.codigo)
        request = MateriaDetalhes(codigo = materia.codigo)
        request.unpack()
        print(request.body.keys())
        DadosBasicosMateria.fromJson(request.body['DadosBasicosMateria'],materia)
        materia.OrigemMateria = OrigemMateria.fromJson(request.body['OrigemMateria']) if 'OrigemMateria' in request.body else None
        if('Classificacoes' in request.body):
            [materia.classificacao.add(Classificacao.fromJson(x)) for x in request.body['Classificacoes']['Classificacao']]
        if('DecisaoEDestino' in request.body):
            Decisao.fromJson(request.body['DecisaoEDestino']['Decisao'],materia)
            Destino.fromJson(request.body['DecisaoEDestino']['Destino'],materia)
        if('Assunto' in request.body):
            [materia.assunto.add(Assunto.fromJson({x:request.body['Assunto'][x]})) for x in request.body['Assunto'].keys()]
        if('MateriasRelacionadas' in request.body):
            [x.MateriaRelacionada.add(Materia.objects.get(codigo=x['CodigoMateria'])) for x in request.body['MateriasRelacionadas']['MateriaRelacionada']]
        if('MateriasAnexadas' in request.body):
            [x.MateriaAnexada.add(Materia.objects.get(codigo=x['CodigoMateria'])) for x in request.body['MateriasAnexadas']['MateriaAnexada']]

def atualizaMovimentacoes():  
    materias = Materia.objects.filter(autuacao__isnull=True).order_by('-data')
    for materia in materias:
        print(materia.codigo)
        request = MateriaMovimentacoes(codigo = materia.codigo)
        request.unpack()
        [materia.autuacao.add(Autuacao.fromJson(x)) for x in request.body['Autuacoes']['Autuacao']]
        [materia.despacho.add(Despacho.fromJson(x)) for x in request.body['Despachos']['Despacho']] if 'Despachos' in request.body else None
        [materia.prazo.add(Prazo.fromJson(x)) for x in request.body['Prazos']['Prazo']] if 'Prazos' in request.body else None
        [materia.ordemDoDia.add(OrdemDoDia.fromJson(x)) for x in request.body['OrdensDoDia']['OrdemDoDia']] if 'OrdensDoDia' in request.body else None

    pass

# Para arquivo, exemplo
# r = requests.get(url,stream=True)
# f = io.BytesIO(r.content)
# pdf = PdfReader(f)
# text = ''
# for page in pdf.pages:
#     text += page.extract_text() + '\n'

