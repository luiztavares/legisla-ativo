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

    def unpack(self):
        self.get()
        try:
            self.body = self.body['PesquisaBasicaMateria']['Materias']['Materia']
        except:
            self.body = []

class MateriaAutoria(models.Model,Request):
    'Obtém a autoria de uma matéria'

    codigo = models.BigIntegerField(primary_key=True) # Código (ID) da matéria. Identificador único da matéria.
    v = models.IntegerField() # (opcional) - Versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/autoria/{self.codigo}'
    
    def unpack(self):
        self.get()
        try:
            self.body = self.body['AutoriaMateria']['Materia']['Autoria']['Autor']
        except:
            self.body = []

class MateriaDetalhes(models.Model,Request):
    'Obtém as atualizações mais recentes em uma matéria'

    codigo = models.BigIntegerField() # Código da matéria no banco de dados
    v = models.IntegerField() # (opcional) - Versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/{self.codigo}'

    def unpack(self):
        self.get()
        try:
            self.body = self.body['DetalheMateria']['Materia']
        except:
            self.body = []

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

    def unpack(self):
        self.get()
        try:
            self.body = self.body['EmendaMateria']['Materia']['Emendas']['Emenda']
        except:
            self.body = []

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

class MateriaMovimentacoes(models.Model,Request):
    'Obtém a movimentação da matéria, incluindo tramitação, prazos, despachos, situação'

    codigo = models.BigIntegerField(primary_key=True) # Código (ID) da matéria. Identificador único da matéria.
    dataref = models.CharField(max_length=8) # (opcional), formato YYYYMMDD - Data de referência para filtrar tramitações
    v = models.IntegerField() # (opcional) - Versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/movimentacoes/{self.codigo}'

    def unpack(self):
        self.get()
        try:
            self.body = self.body['MovimentacaoMateria']['Materia']
        except:
            self.body = []

class MateriaVotacoes(models.Model,Request):
    'Obtém as votações de uma matéria'

    codigo = models.BigIntegerField(primary_key=True) # Código (ID) da matéria. Identificador único da matéria.
    v = models.IntegerField() # (opcional) - Versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/votacoes/{self.codigo}'

class MateriaListaPrazo(models.Model,Request):
    'Obtém a lista de matérias cumprindo prazo em plenário ou comissões. Se quiser que retorne todos os tipos de prazo, informe "0" (zero) para o código do prazo.'

    codPrazo = models.BigIntegerField(primary_key=True, default=0) # Código do tipo do prazo
    comissao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    v = models.IntegerField() # (opcional) - Versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/lista/prazo/{self.codPrazo}'

class MateriaLegislaturaAtual(models.Model,Request):
    "Lista as matérias que estão em tramitação ou que tramitaram na Legislatura atual. Atenção: para pesquisar por período da última atualização, utilize o serviço de matérias atualizadas."
    
    url = 'https://legis.senado.leg.br/dadosabertos/materia/legislaturaatual?'
    class Boleana(models.TextChoices):
        S = 'S', "Sim"
        N = 'N', "Não"

    ano = models.CharField(max_length=4)  # (opcional) ano da matéria
    numero = models.BigIntegerField() # (opcional) número da matéria
    sigla = models.CharField(max_length=50) # (opcional) sigla da matéria
    tramitando = models.CharField(max_length=1,choices=Boleana.choices) # (opcional) indica se retorna apenas as matérias que estão tramitando ("S") ou não ("N")
    v = models.CharField(max_length=10) # (opcional) versão do serviço

class MateriaTramintando(models.Model,Request):
    "Lista as matérias que estão em tramitação (não tem informações de comissões)"
    
    url = 'https://legis.senado.leg.br/dadosabertos/materia/tramitando?'

    ano = models.CharField(max_length=4)  # (opcional) ano da matéria
    data = models.CharField(max_length=8) # (opcional) formato (YYYYMMDD) - Parâmetro usado para que sejam retornadas apenas as matérias cuja última atualização é igual ou posterior à data informada
    hora = models.CharField(max_length=6) # (opcional) formato (HHMISS) - Onde HH é no padrão 24 horas e MI representa os minutos, com 2 dígitos - parâmetro usado para que sejam retornadas apenas as matérias cuja hora da última atualização é igual ou posterior à hora informada. Deve ser informado apenas se a data também for informada.
    numero = models.BigIntegerField() # (opcional) número da matéria
    sigla = models.CharField(max_length=50) # (opcional) sigla da matéria
    v = models.CharField(max_length=10) # (opcional) versão do serviço

class PlenarioResultadoVetoDispositivo(models.Model,Request):
    'SERVICO ESTRNAHO Obtém o resultado da votação nominal de um dispositivo de veto'

    codigo = models.BigIntegerField() # código do dispositivo
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://www.congressonacional.leg.br/dados/plenario/resultado/veto/dispositivo/{self.codigo}'

class PlenarioResultadoVeto(models.Model,Request):
    'Obtém o resultado da votação nominal de um item de veto'

    codigo = models.BigIntegerField() # código do Veto
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://www.congressonacional.leg.br/dados/plenario/resultado/veto/{self.codigo}'

class PlenarioResultadoVetoMateria(models.Model,Request):
    'Obtém o resultado da votação nominal de vetos de uma matéria'

    codigo = models.BigIntegerField() # código da matéria
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://www.congressonacional.leg.br/dados/plenario/resultado/veto/materia/{self.codigo}'


class SenadorRelatorias(models.Model,Request):
    'Obtém as matérias de relatoria de um senador'

    codigo = models.BigIntegerField() # código do senador
    ano = models.CharField(max_length=4) # (opcional) - Ano da matéria - retorna apenas as matérias do ano informado	n/a
    comissao = models.CharField(max_length=10) # (opcional) - Sigla da comissão - retorna apenas as relatorias da comissão informada.	n/a
    numero = models.CharField(max_length=10) # (opcional) - Número da matéria - retorna apenas as matérias do número informado.	n/a
    sigla = models.CharField(max_length=20) # (opcional) - Sigla da matéria - retorna apenas as matérias da sigla informada.	n/a
    tramitando = models.CharField(max_length=1) # (opcional) (S ou N) - retorna apenas as matérias que estão tramitando (S) ou apenas as que não estão (N). Se não for informado, retorna ambas.	n/a
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f' https://legis.senado.leg.br/dadosabertos/senador/{self.codigo}/relatorias'

class SenadorAutorias(models.Model,Request):
    'Obtém as matérias de autoria de um senador'

    codigo = models.BigIntegerField() # código do senador
    ano = models.CharField(max_length=4) # (opcional) - Ano da matéria - retorna apenas as matérias do ano informado	n/a
    numero = models.CharField(max_length=10) # (opcional) - Número da matéria - retorna apenas as matérias do número informado.	n/a
    primeiro = models.CharField(max_length=1) # (opcional) (S ou N) - retorna apenas as matérias cujo senador é o primeiro autor, ou seja, o autor principal (S) ou apenas as que o senador é coautor (N).	
    sigla = models.CharField(max_length=20) # (opcional) - Sigla da matéria - retorna apenas as matérias da sigla informada.	n/a
    tramitando = models.CharField(max_length=1) # (opcional) (S ou N) - retorna apenas as matérias que estão tramitando (S) ou apenas as que não estão (N). Se não for informado, retorna ambas.	n/a
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f' https://legis.senado.leg.br/dadosabertos/senador/{self.codigo}/autorias'

class SenadorApartes(models.Model,Request):
    'Obtém a relação de apartes do senador'

    codigo = models.BigIntegerField() # código do senador
    casa = models.CharField(max_length=2) # (opcional) - Sigla da casa aonde ocorre o pronunciamento - SF (Senado), CD (Câmara), CN (Congresso), PR (Presidência), CR (Comissão Representativa do Congresso), AC (Assembléia Constituinte)
    dataFim = models.CharField(max_length=8) # (opcional) - Data de fim do período da pesquisa no formato AAAAMMDD
    dataInicio = models.CharField(max_length=8) # (opcional) - Data de fim do período da pesquisa no formato AAAAMMDD
    numeroSessao = models.CharField(max_length=10) # (opcional) - Número da sessão plenária
    tipoSessao = models.CharField(max_length=10) # (opcional) - Tipo da sessão plenária (veja serviço que lista os tipos de sessão)
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f' https://legis.senado.leg.br/dadosabertos/senador/{self.codigo}/apartes'

class SenadorDiscursos(models.Model,Request):
    'Obtém a relação de discursos do senador'

    codigo = models.BigIntegerField() # código do senador
    casa = models.CharField(max_length=2) # (opcional) - Sigla da casa aonde ocorre o pronunciamento - SF (Senado), CD (Câmara), CN (Congresso), PR (Presidência), CR (Comissão Representativa do Congresso), AC (Assembléia Constituinte)
    dataFim = models.CharField(max_length=8) # (opcional) - Data de fim do período da pesquisa no formato AAAAMMDD
    dataInicio = models.CharField(max_length=8) # (opcional) - Data de fim do período da pesquisa no formato AAAAMMDD
    numeroSessao = models.CharField(max_length=10) # (opcional) - Número da sessão plenária
    tipoSessao = models.CharField(max_length=10) # (opcional) - Tipo da sessão plenária (veja serviço que lista os tipos de sessão)
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f' https://legis.senado.leg.br/dadosabertos/senador/{self.codigo}/discursos'

class PlenarioListaDiscursos(models.Model,Request):
    'Obtém a lista de discursos da(s) sessão(ões) que ocorreram dentro do período informado'

    dataFim = models.CharField(max_length=8) # Data fim para as sessões da consulta no formato AAAAMMDD``
    dataInicio = models.CharField(max_length=8) # Data inicial para as sessões da consulta no formato AAAAMMDD
    siglaCasa = models.CharField(max_length=2) # ((opcional) - Sigla da casa (SF = Senado Federal, CN = Congresso Nacional)
    numeroSessao = models.CharField(max_length=10) # (opcional) - Número da sessao
    tipoSessao = models.CharField(max_length=10) # (opcional) - Sigla do tipo de sessão
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/plenario/lista/discursos/{self.dataInicio}/{self.dataInicio}'


class SenadorLiderancas(models.Model,Request):
    'Obtém os cargos de liderança de um senador'

    codigo = models.BigIntegerField() # Código do senador
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/senador/{self.codigo}/liderancas'

class SenadorCargos(models.Model,Request):
    'Obtém os cargos de um senador'

    codigo = models.BigIntegerField() # Código do senador
    comissao = models.CharField(max_length=20) # (opcional) - Sigla da comissão - retorna apenas os cargos na comissão informada.
    indAtivos = models.CharField(max_length=1) # (opcional) - Se "S" retorna apenas os cargos atuais, se "N" retorna apenas os já finalizados
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/senador/{self.codigo}/cargos'


class SenadorComissoes(models.Model,Request):
    'Obtém Comissoes de um senador'

    codigo = models.BigIntegerField() # Código do senador
    comissao = models.CharField(max_length=20) # (opcional) - Sigla da comissão - retorna apenas os cargos na comissão informada.
    indAtivos = models.CharField(max_length=1) # (opcional) - Se "S" retorna apenas os cargos atuais, se "N" retorna apenas os já finalizados
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/senador/{self.codigo}/comissoes'

class Senador(models.Model,Request):
    'Obtém detalhes de um senador'

    codigo = models.BigIntegerField() # Código do senador
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/senador/{self.codigo}'

class SenadorHistorico(models.Model,Request):
    'Obtém todos os detalhes de um parlamentar no(s) mandato(s) como senador (mandato atual e anteriores, se houver)'

    codigo = models.BigIntegerField() # Código do senador
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/senador/{self.codigo}/historico'

class SenadorMandatos(models.Model,Request):
    'Obtém os mandatos que o senador já teve'

    codigo = models.BigIntegerField() # Código do senador
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/senador/{self.codigo}/mandatos'


class SenadorFiliacoes(models.Model,Request):
    'Obtém as filiações partidárias que o senador já teve'

    codigo = models.BigIntegerField() # Código do senador
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/senador/{self.codigo}/filiacoes'


class SenadorVotacoes(models.Model,Request):
    'Obtém as votações de um senador'

    codigo = models.BigIntegerField() # Código do senador
    ano = models.CharField(max_length=4) # (opcional) - Ano da matéria - retorna apenas as matérias do ano informado	n/a
    numero = models.BigIntegerField() # (opcional) - Número da matéria - retorna apenas as matérias do número informado.
    sigla = models.CharField(max_length=50) # (opcional) sigla da matéria
    tramitando = models.CharField(max_length=1) # (opcional) (S ou N) - retorna apenas as matérias que estão tramitando (S) ou apenas as que não estão (N). Se não for informado, retorna ambas.	n/a
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/senador/{self.codigo}/votacoes'

class SenadorListaLegislatura(models.Model,Request):
    'Obtém a lista de senadores de uma legislatura'

    legislatura = models.BigIntegerField() # Número da legislatura
    exercicio = models.CharField(max_length=1) # (opcional) - Filtrar apenas parlamentares que entraram em exercício "S" (sim) ou apenas os que não entraram "N" (não)
    participacao = models.CharField(max_length=1) # (opcional) - Tipo de participação: "T" (titular) / "S" (suplente)
    uf = models.CharField(max_length=2) # (opcional) - Sigla da UF do mandato
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/senador/lista/legislatura/{self.legislatura}'

class SenadorListaLegislaturaIntervalo(models.Model,Request):
    'Obtém a lista de senadores de um intervalo de legislatura'

    legislaturaFim = models.BigIntegerField() # Número da legislatura
    legislaturaInicio = models.BigIntegerField() # Número da legislatura
    exercicio = models.CharField(max_length=1) # (opcional) - Filtrar apenas parlamentares que entraram em exercício "S" (sim) ou apenas os que não entraram "N" (não)
    participacao = models.CharField(max_length=1) # (opcional) - Tipo de participação: "T" (titular) / "S" (suplente)
    uf = models.CharField(max_length=2) # (opcional) - Sigla da UF do mandato
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/senador/lista/legislatura/{self.legislaturaInicio}/{self.legislaturaFim}'

class PlenarioAgenda(models.Model,Request):
    'Obtém a agenda do dia do plenário do Congresso'

    data = models.CharField(max_length=8) # Número da legislatura
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://www.congressonacional.leg.br/dados/plenario/agenda/{self.data}'

class PlenarioLegislaturaSessao(models.Model,Request):
    'Obtém a agenda do dia do plenário do Congresso'

    dataSessaoLeg = models.CharField(max_length=8) # Número da legislatura
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/plenario/legislatura/sessaoLegislativa/{self.dataSessaoLeg}'

class ComissaoComposicaoAtualMista(models.Model,Request):
    'Obtém a agenda do dia do plenário do Congresso'

    codigo = models.CharField(max_length=8) # código da comissão
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://www.congressonacional.leg.br/dados/comissao/composicao/atual/mista/{self.codigo}'

class ComissaoComposicaoResumidaMistaPeriodo(models.Model,Request):
    'Obtém a composição resumida de uma comissão mista, por períodor'

    codigo = models.BigIntegerField() # código da comissao
    dataFim = models.CharField(max_length=8) # (opcional) - Data de fim do período da pesquisa no formato AAAAMMDD
    dataInicio = models.CharField(max_length=8) # (opcional) - Data de fim do período da pesquisa no formato AAAAMMDD
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://www.congressonacional.leg.br/dados/comissao/composicao/resumida/mista/{self.codigo}/{self.dataInicio}/{self.dataFim}'


class ComissaoTipo(models.Model,Request):
    'Obtém a composição das Comissões do Congresso Nacional'

    tipo = models.CharField(max_length=20) # tipo da comissão: cpmi, veto, permanente, mpv, mistaEspecial, mesa, trabalhoCCS, representativa
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://www.congressonacional.leg.br/dados/comissao/lista/{self.tipo}'

class MateriaDistribuicaoAutoria(models.Model,Request):
    'Obtém a distribuição de autoria de matérias de um senador. Necessário informar o código do parlamentar.'

    codParlamentar = models.CharField(max_length=20) # (opcional) - Código do parlamentar	
    siglaComissao = models.CharField(max_length=20) # (opcional) - Sigla da comissão
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/distribuicao/autoria'

class MateriaDistribuicaoAutoriaComissao(models.Model,Request):
    'Obtém a distribuição de autoria de matérias em uma comissão'

    codParlamentar = models.CharField(max_length=20) # (opcional) - Código do parlamentar	
    siglaComissao = models.CharField(max_length=20) # (opcional) - Sigla da comissão
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/materia/distribuicao/autoria/{self.siglaComissao}'


class LegislacaoLista(models.Model,Request):
    'Obtém a lista de normas da base do Senado Federal ATENÇÃO: é necessário informar uma das seguintes combinações de parâmetros: "numero" ou "tipo" e "numero" ou "tipo" e "ano" ou "numero" e "ano" O parâmetro "versao" é opcional'

    ano	= models.CharField(max_length=4) # (opcional) - Ano da norma
    complemento = models.CharField(max_length=100) # (opcional) - letra de complemento (somente para versão 3 ou posterior)
    data = models.CharField(max_length=8) # (opcional) formato (YYYYMMDD) - Data da assinatura da norma (somente para versão 3 ou posterior)
    ident = models.CharField(max_length=10) # (opcional) - letra de identificação (somente para versão 3 ou posterior)
    numero = models.IntegerField() # (opcional) - Número da norma
    reedicao = models.BigIntegerField() # (opcional) - número sequencial e reedição (somente para versão 3 ou posterior)
    seq = models.BigIntegerField() # (opcional) - número sequencial da assinatura da norma na data (somente para versão 3 ou posterior)
    tipo = models.CharField(max_length=20) # (opcional) - Sigla do tipo da norma
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/legislacao/lista'

class LegislacaoTermos(models.Model,Request):
    'Obtém a lista de normas da base do Senado Federal ATENÇÃO: é necessário informar uma das seguintes combinações de parâmetros: "numero" ou "tipo" e "numero" ou "tipo" e "ano" ou "numero" e "ano" O parâmetro "versao" é opcional'

    termo	= models.TextField() # Filtro de palavras
    tipo = models.CharField(max_length=20) # (opcional) - Sigla do tipo de termo
    v = models.CharField(max_length=10) # (opcional) versão de serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/legislacao/termos'

class Legislacao(models.Model,Request):
    'Obtém detalhes de uma norma através do código'

    codigo = models.BigIntegerField() # código da comissao
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/legislacao/{self.codigo}'

class LegislacaoData(models.Model,Request):
    'Obtém detalhes do documento através do tipo/número/ano ou através da data de assinatura/sequencial'

    anoseq = models.BigIntegerField() # ano da data de assinatura do documento ou sequencial
    numdata = models.BigIntegerField() # número do documento ou data da assinatura
    tipo = models.CharField(max_length=20) # Sigla do tipo do documento
    v = models.CharField(max_length=10) # (opcional) versão do serviço

    @property
    def url(self):
        return f'https://legis.senado.leg.br/dadosabertos/legislacao/{self.tipo}/{self.numdata}/{self.anoseq}'


class HorasExtras(models.Model,Request):
    'Obtém detalhes do documento através do tipo/número/ano ou através da data de assinatura/sequencial'

    ano = models.CharField(max_length=4,help_text='path') # ano 
    mes = models.CharField(max_length=2,help_text='path') # mes

    @property
    def url(self):
        return f'https://adm.senado.gov.br/dadosabertos-gestaopessoas/api/dadosabertos/v1/horas-extras/{self.ano}/{self.mes}'
