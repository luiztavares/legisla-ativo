from .models.api import *
from .models.database import *

from datetime import date
from dateutil.relativedelta import relativedelta

def atualizaTodasAsMaterias():
    try:
        dataInicioApresentacao = Materia.objects.latest('data').data
    except:
        dataInicioApresentacao = date(1946,1,1)
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
    materias = Materia.objects.filter(dadosbasicosmateria__isnull=True)
    for materia in materias:
        request = MateriaDetalhes(codigo = materia.codigo)
        request.unpack()
        print(materia.codigo)
        dadosBasicosMateria = DadosBasicosMateria.fromJson(request.body['DadosBasicosMateria'])
        classificacoes = [x for x in Classificacao.fromJson(request.body['Classificacoes']['Classificacao'])]
        decisao = Decisao(request.body['DecisaoEDestino']['Decisao'])
        destino = Destino(request.body['DecisaoEDestino']['Destino'])



def atualizaEmendas():

    pass
