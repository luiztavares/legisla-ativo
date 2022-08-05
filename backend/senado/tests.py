from django.test import TestCase
from .models.api import *

from datetime import date
from dateutil.relativedelta import relativedelta

def testPesquisaMateriaService():
    FIRST_DATE = date(2022,1,1)
    last_date = FIRST_DATE
    dataInicioApresentacao = last_date
    dataFimApresentacao = dataInicioApresentacao + relativedelta(years=1) - relativedelta(days=1)

    materia_pesquisa_lista = PesquisaMateriaService(
        dataInicioApresentacao=dataInicioApresentacao.strftime('%Y%m%d'),
        dataFimApresentacao=dataFimApresentacao.strftime('%Y%m%d'),
    )

    print(f'inicio: {dataInicioApresentacao}, fim: {dataFimApresentacao}')
    return materia_pesquisa_lista.get()

def testAutoriaRequest():
    autoria = MateriaAutoria(codigo=152001).get()

def testMateriaAtualizacoes():
    materiaAtualizacoes = MateriaAtualizacoes(codigo=152001,numdias=365).get()
    print(materiaAtualizacoes)

def testMateriaEmendas():
    materiaEmendas = MateriaEmendas(codigo=152001).get()
    print(materiaEmendas)

def testMateriaRelatorias():
    materiaRelatorias = MateriaRelatorias(codigo=152001).get()
    print(materiaRelatorias)

def testMateriaTextos():
    materiaRelatorias = MateriaTextos(codigo=152001).get()
    print(materiaRelatorias)

testMateriaTextos()

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
