from django.shortcuts import render
from database.models import *
from request.models import *

from datetime import date
from dateutil.relativedelta import relativedelta


# Create your views here.

def updateMateriaPesquisaLista():
    FIRST_DATE = date(1946,1,1)
    try:
        last_date = Materia.objects.latest('data').data
    except:
        last_date = FIRST_DATE
    
    dataInicioApresentacao = last_date
    dataFimApresentacao = dataInicioApresentacao + relativedelta(years=1) - relativedelta(days=1)

    def updateAno():
        materia_pesquisa_lista = MateriaPesquisaLista(
            dataInicioApresentacao=dataInicioApresentacao.strftime('%Y%m%d'),
            dataFimApresentacao=dataFimApresentacao.strftime('%Y%m%d'),
        )

        print(f'inicio: {dataInicioApresentacao}, fim: {dataFimApresentacao}')
        materias_json = materia_pesquisa_lista.get()
        
        try:
            materias_json = materias_json['PesquisaBasicaMateria']['Materias']['Materia']
        except:
            print('sem matérias')
            return

        for materia_json in materias_json:
            materia = Materia.from_json(materia_json)
            materia.save()
    
    while (dataFimApresentacao < date.today()):
        dataInicioApresentacao = dataFimApresentacao + relativedelta(days=1)
        dataFimApresentacao = dataInicioApresentacao + relativedelta(years=1) - relativedelta(days=1)

        updateAno()

def updateAutoria():
    for materia in Materia.objects.filter(autoria=None):
        print(materia)

        autoria = AutoriaRequest(codigo=materia.codigo).get()
        if('Autoria' in autoria['AutoriaMateria']['Materia']):
            for autorJson in autoria['AutoriaMateria']['Materia']['Autoria']['Autor']:
                autor = Autoria.fromJson(autorJson)
                autor.save()
                autor.materia.add(materia)
        if( 'Iniciativa' in autoria['AutoriaMateria']['Materia']):
            iniciativa = Iniciativa.fromJson(autoria['AutoriaMateria']['Materia']['Iniciativa'])
            iniciativa.save()
            iniciativa.materia.add(materia)
