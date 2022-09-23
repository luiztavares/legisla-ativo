from django.test import TestCase
from .models.api import *
from .services import *

from datetime import date
from dateutil.relativedelta import relativedelta


def testPesquisaMateriaService():
    FIRST_DATE = date(2020,1,1)
    last_date = FIRST_DATE
    dataInicioApresentacao = last_date
    dataFimApresentacao = dataInicioApresentacao + relativedelta(years=1) - relativedelta(days=1)

    materia_pesquisa_lista = PesquisaMateriaService(
        dataInicioApresentacao=dataInicioApresentacao.strftime('%Y%m%d'),
        dataFimApresentacao=dataFimApresentacao.strftime('%Y%m%d'),
    )
    materia_pesquisa_lista.unpack()

    print(f'inicio: {dataInicioApresentacao}, fim: {dataFimApresentacao}, {len(materia_pesquisa_lista.body)}')
    return 

def testAutoriaRequest():
    autoria = MateriaAutoria(codigo=152001).get()

def testMateriaAtualizacoes():
    materiaAtualizacoes = MateriaAtualizacoes(codigo=152001,numdias=999999).get()
    print(materiaAtualizacoes)

def testMateriaEmendas():
    materiaEmendas = MateriaEmendas(codigo=152001).get()
    print(materiaEmendas)

def testMateriaRelatorias():
    materiaRelatorias = MateriaRelatorias(codigo=152001).get()
    print(materiaRelatorias)

def testMateriaTextos():
    materiaTextos = MateriaTextos(codigo=152001).get()
    print(materiaTextos)

def testMateriaMovimentacoes():
    materiaMovimentacoes = MateriaMovimentacoes(codigo=152001).get()
    print(materiaMovimentacoes)

def testMateriaVotacoes():
    materiaVotacoes = MateriaVotacoes(codigo=137178).get()
    print(materiaVotacoes)

def testMateriaListaPrazo():
    materiaListaPrazo = MateriaListaPrazo().get()
    print(materiaListaPrazo)

def testMateriaLegislaturaAtual():
    materia = MateriaLegislaturaAtual().get()
    print(materia)

def testMateriaTramitando():
    materia = MateriaTramintando().get()
    print(materia)

def testPlenarioResultadoVetoDispositivo():
    veto = PlenarioResultadoVetoDispositivo(codigo=137178).get()
    print(veto)

def testPlenarioResultadoVeto():
    veto = PlenarioResultadoVeto(codigo=11762).get()
    print(veto)

def testPlenarioResultadoVetoMateria():
    veto = PlenarioResultadoVetoMateria(codigo=137178).get()
    print(veto)

def testSenadorRelatorias():
    relatorias = SenadorRelatorias(codigo=4981).get()
    print(relatorias)

def testSenadorAutorias():
    autorias = SenadorAutorias(codigo=4981).get()
    print(autorias)

def testSenadorApartes():
    apartes = SenadorApartes(codigo=4981).get()
    print(apartes)

def testSenadorDiscursos():
    discursos = SenadorDiscursos(codigo=4981).get()
    print(discursos)

def testPlenarioListaDiscursos():
    discursos = PlenarioListaDiscursos(dataInicio='20130301',dataFim='20130331').get()
    print(discursos)

def testSenadorLiderancas():
    liderancas = SenadorLiderancas(codigo=4981).get()
    print(liderancas)

def testSenadorCargos():
    cargos = SenadorCargos(codigo=4981).get()
    print(cargos)

def testSenadorComissoes():
    comissoes = SenadorComissoes(codigo=4981).get()
    print(comissoes)

def testSenador():
    senador = Senador(codigo=4981).get()
    print(senador)

def testSenadorHistorico():
    senador = SenadorHistorico(codigo=4981).get()
    print(senador)

def testSenadorMandatos():
    mandatos = SenadorMandatos(codigo=4981).get()
    print(mandatos)

def testSenadorFiliacoes():
    filiacoes = SenadorFiliacoes(codigo=4981).get()
    print(filiacoes)

def testSenadorVotacoes():
    votacoes = SenadorVotacoes(codigo=4981).get()
    print(votacoes)

def testSenadorListaLegislatura():
    senador = SenadorListaLegislatura(legislatura=22).get()
    print(senador)

def testSenadorListaLegislatura():
    senador = SenadorListaLegislaturaIntervalo(legislaturaInicio=22,legislaturaFim=25,).get()
    print(senador)

def testPlenarioAgenda():
    agenda = PlenarioAgenda(data='20220510',).get()
    print(agenda)

def testPlenarioLegislaturaSessao():
    agenda = PlenarioLegislaturaSessao(dataSessaoLeg='20210510',).get()
    print(agenda)

def testComissaoComposicaoAtualMista():
    comissao = ComissaoComposicaoAtualMista(codigo='20210510',).get()
    print(comissao)

def testComissaoTipo():
    comissao = ComissaoTipo(tipo='cpmi',).get()
    print(comissao)

def testMateriaDistribuicaoAutoria():
    comissao = MateriaDistribuicaoAutoria(siglaComissao='CCJ').get()
    print(comissao)

def testLegislacaoLista():
    leis = LegislacaoLista(ano=2021).get()
    print(leis)

def testLegislacaoTermos():
    termo = LegislacaoTermos().get()
    print(termo)

def testLegislacao():
    termo = Legislacao(codigo=397127).get()
    print(termo)

def testLegislacaoData():
    termo = LegislacaoData(tipo='RSF',numdata=57,anoseq=1985).get()
    print(termo)

def testHorasExtras():
    horas = HorasExtras(ano='2022',mes='03').get()
    print(horas)

# atualizaTodosAutores()
atualizaDetalhes()
# atualizaTodasAsMaterias()

# Create your tests here.

# def updateMateriaPesquisaLista():
#     FIRST_DATE = date(1946,1,1)
#     try:
#         last_date = Materia.objects.latest('data').data
#     except:
#         last_date = FIRST_DATE
    
#     dataInicioApresentacao = last_date
#     dataFimApresentacao = dataInicioApresentacao + relativedelta(years=1) - relativedelta(days=1)

#     def updateAno():
#         materia_pesquisa_lista = MateriaPesquisaLista(
#             dataInicioApresentacao=dataInicioApresentacao.strftime('%Y%m%d'),
#             dataFimApresentacao=dataFimApresentacao.strftime('%Y%m%d'),
#         )

#         print(f'inicio: {dataInicioApresentacao}, fim: {dataFimApresentacao}')
#         materias_json = materia_pesquisa_lista.get()
        
#         try:
#             materias_json = materias_json['PesquisaBasicaMateria']['Materias']['Materia']
#         except:
#             print('sem matérias')
#             return

#         for materia_json in materias_json:
#             materia = Materia.from_json(materia_json)
#             materia.save()
    
#     while (dataFimApresentacao < date.today()):
#         dataInicioApresentacao = dataFimApresentacao + relativedelta(days=1)
#         dataFimApresentacao = dataInicioApresentacao + relativedelta(years=1) - relativedelta(days=1)

#         updateAno()

# def updateAutoria():
#     for materia in Materia.objects.filter(autoria=None):
#         print(materia)

#         autoria = AutoriaRequest(codigo=materia.codigo).get()
#         if('Autoria' in autoria['AutoriaMateria']['Materia']):
#             for autorJson in autoria['AutoriaMateria']['Materia']['Autoria']['Autor']:
#                 autor = Autoria.fromJson(autorJson)
#                 autor.save()
#                 materia.autoria.add(autor)
#         if( 'Iniciativa' in autoria['AutoriaMateria']['Materia']):
#             iniciativa = Iniciativa.fromJson(autoria['AutoriaMateria']['Materia']['Iniciativa'])
#             iniciativa.save()
#             iniciativa.materia.add(materia)
