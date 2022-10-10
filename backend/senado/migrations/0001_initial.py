# Generated by Django 3.2.16 on 2022-10-09 22:56

import core.tools
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('codigo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Autoria',
            fields=[
                ('nomeAutor', models.TextField(primary_key=True, serialize=False)),
                ('siglaTipoAutor', models.CharField(max_length=200)),
                ('descricaoTipoAutor', models.CharField(max_length=200)),
                ('numOrdemAutor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Autuacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumeroAutuacao', models.BigIntegerField()),
                ('DescricaoAutuacao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Classificacao',
            fields=[
                ('codigoClasse', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descricaoClasse', models.CharField(max_length=200)),
                ('descricaoClasseHierarquica', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ComissaoComposicaoAtualMista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='ComissaoComposicaoResumidaMistaPeriodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('dataFim', models.CharField(max_length=8)),
                ('dataInicio', models.CharField(max_length=8)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='ComissaoTipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataDespacho', models.DateField()),
                ('TipoMotivacao', models.TextField()),
                ('IndicadorDespachoCancelado', models.CharField(max_length=50)),
                ('Observacao1Despacho', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Destinatario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumeroOrdem', models.IntegerField()),
                ('TipoDeliberacao', models.CharField(max_length=100)),
                ('CodigoColegiado', models.CharField(max_length=50)),
                ('SiglaColegiado', models.CharField(max_length=50)),
                ('SiglaCompleta', models.CharField(max_length=50)),
                ('SiglaCasaColegiado', models.CharField(max_length=50)),
                ('NomeColegiado', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Emenda',
            fields=[
                ('codigoEmenda', models.BigIntegerField(primary_key=True, serialize=False)),
                ('numeroEmenda', models.CharField(max_length=20)),
                ('dataApresentacao', models.DateField()),
                ('colegiadoApresentacao', models.CharField(max_length=20)),
                ('descricaoTurno', models.CharField(max_length=100)),
                ('descricaoTipoEmenda', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HorasExtras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(help_text='path', max_length=4)),
                ('mes', models.CharField(help_text='path', max_length=2)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='IdentificacaoComissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoComissao', models.CharField(max_length=50)),
                ('SiglaComissao', models.CharField(max_length=50)),
                ('NomeComissao', models.TextField()),
                ('SiglaCasaComissao', models.CharField(max_length=50)),
                ('NomeCasaComissao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IndexacaoMateria',
            fields=[
                ('index', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Legislacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='LegislacaoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anoseq', models.BigIntegerField()),
                ('numdata', models.BigIntegerField()),
                ('tipo', models.CharField(max_length=20)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='LegislacaoLista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(max_length=4)),
                ('complemento', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=8)),
                ('ident', models.CharField(max_length=10)),
                ('numero', models.IntegerField()),
                ('reedicao', models.BigIntegerField()),
                ('seq', models.BigIntegerField()),
                ('tipo', models.CharField(max_length=20)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='LegislacaoTermos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termo', models.TextField()),
                ('tipo', models.CharField(max_length=20)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('CodigoLocal', models.BigIntegerField(primary_key=True, serialize=False)),
                ('SiglaLocal', models.CharField(max_length=100)),
                ('NomeLocal', models.TextField()),
                ('SiglaCasaLocal', models.CharField(max_length=50)),
                ('NomeCasaLocal', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MateriaAtualizacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('numdias', models.BigIntegerField(default=30)),
                ('v', models.IntegerField()),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='MateriaAutoria',
            fields=[
                ('codigo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('v', models.IntegerField()),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='MateriaDetalhes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('v', models.IntegerField()),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='MateriaDistribuicaoAutoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codParlamentar', models.CharField(max_length=20)),
                ('siglaComissao', models.CharField(max_length=20)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='MateriaDistribuicaoAutoriaComissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codParlamentar', models.CharField(max_length=20)),
                ('siglaComissao', models.CharField(max_length=20)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='MateriaEmendas',
            fields=[
                ('codigo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('v', models.IntegerField()),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='MateriaLegislaturaAtual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(max_length=4)),
                ('numero', models.BigIntegerField()),
                ('sigla', models.CharField(max_length=50)),
                ('tramitando', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='MateriaListaPrazo',
            fields=[
                ('codPrazo', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('comissao', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('v', models.IntegerField()),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='MateriaMovimentacoes',
            fields=[
                ('codigo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('dataref', models.CharField(max_length=8)),
                ('v', models.IntegerField()),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='MateriaRelatorias',
            fields=[
                ('codigo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('v', models.IntegerField()),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='MateriaTextos',
            fields=[
                ('codigo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('v', models.IntegerField()),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='MateriaTramintando',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(max_length=4)),
                ('data', models.CharField(max_length=8)),
                ('hora', models.CharField(max_length=6)),
                ('numero', models.BigIntegerField()),
                ('sigla', models.CharField(max_length=50)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='MateriaVotacoes',
            fields=[
                ('codigo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('v', models.IntegerField()),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='NaturezaMateria',
            fields=[
                ('codigoNatureza', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nomeNatureza', models.CharField(max_length=100)),
                ('descricaoNatureza', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrigemMateria',
            fields=[
                ('NomePoderOrigem', models.TextField(null=True)),
                ('SiglaCasaOrigem', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PesquisaMateriaService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(max_length=4)),
                ('anoNorma', models.CharField(max_length=4)),
                ('codigoClasse', models.BigIntegerField()),
                ('codigoConteudo', models.BigIntegerField()),
                ('dataFimApresentacao', models.CharField(max_length=8)),
                ('dataInicioApresentacao', models.CharField(max_length=8)),
                ('nomeAutor', models.TextField()),
                ('numero', models.BigIntegerField()),
                ('numeroNorma', models.BigIntegerField()),
                ('palavraChave', models.TextField()),
                ('sigla', models.CharField(max_length=50)),
                ('siglaComissaoReq', models.CharField(max_length=50)),
                ('tipoNorma', models.CharField(max_length=50)),
                ('tramitando', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='PlenarioAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=8)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='PlenarioLegislaturaSessao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataSessaoLeg', models.CharField(max_length=8)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='PlenarioListaDiscursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataFim', models.CharField(max_length=8)),
                ('dataInicio', models.CharField(max_length=8)),
                ('siglaCasa', models.CharField(max_length=2)),
                ('numeroSessao', models.CharField(max_length=10)),
                ('tipoSessao', models.CharField(max_length=10)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='PlenarioResultadoVeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='PlenarioResultadoVetoDispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='PlenarioResultadoVetoMateria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='Senador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorApartes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('casa', models.CharField(max_length=2)),
                ('dataFim', models.CharField(max_length=8)),
                ('dataInicio', models.CharField(max_length=8)),
                ('numeroSessao', models.CharField(max_length=10)),
                ('tipoSessao', models.CharField(max_length=10)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorAutorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('ano', models.CharField(max_length=4)),
                ('numero', models.CharField(max_length=10)),
                ('primeiro', models.CharField(max_length=1)),
                ('sigla', models.CharField(max_length=20)),
                ('tramitando', models.CharField(max_length=1)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorCargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('comissao', models.CharField(max_length=20)),
                ('indAtivos', models.CharField(max_length=1)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorComissoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('comissao', models.CharField(max_length=20)),
                ('indAtivos', models.CharField(max_length=1)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorDiscursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('casa', models.CharField(max_length=2)),
                ('dataFim', models.CharField(max_length=8)),
                ('dataInicio', models.CharField(max_length=8)),
                ('numeroSessao', models.CharField(max_length=10)),
                ('tipoSessao', models.CharField(max_length=10)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorFiliacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorHistorico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorLiderancas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorListaLegislatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legislatura', models.BigIntegerField()),
                ('exercicio', models.CharField(max_length=1)),
                ('participacao', models.CharField(max_length=1)),
                ('uf', models.CharField(max_length=2)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorListaLegislaturaIntervalo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legislaturaFim', models.BigIntegerField()),
                ('legislaturaInicio', models.BigIntegerField()),
                ('exercicio', models.CharField(max_length=1)),
                ('participacao', models.CharField(max_length=1)),
                ('uf', models.CharField(max_length=2)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorMandatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorRelatorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('ano', models.CharField(max_length=4)),
                ('comissao', models.CharField(max_length=10)),
                ('numero', models.CharField(max_length=10)),
                ('sigla', models.CharField(max_length=20)),
                ('tramitando', models.CharField(max_length=1)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SenadorVotacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('ano', models.CharField(max_length=4)),
                ('numero', models.BigIntegerField()),
                ('sigla', models.CharField(max_length=50)),
                ('tramitando', models.CharField(max_length=1)),
                ('v', models.CharField(max_length=10)),
            ],
            bases=(models.Model, core.tools.Request),
        ),
        migrations.CreateModel(
            name='SessaoPlenaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoSessao', models.BigIntegerField()),
                ('SiglaCasaSessao', models.CharField(max_length=50)),
                ('NomeCasaSessao', models.TextField()),
                ('CodigoSessaoLegislativa', models.CharField(max_length=50)),
                ('SiglaTipoSessao', models.CharField(max_length=50)),
                ('NumeroSessao', models.BigIntegerField()),
                ('DataSessao', models.DateField()),
                ('HoraInicioSessao', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SituacaoAtual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataSituacao', models.DateField()),
                ('CodigoSituacao', models.BigIntegerField()),
                ('SiglaSituacao', models.CharField(max_length=100)),
                ('DescricaoSituacao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SituacaoIniciada',
            fields=[
                ('SituacaoIniciadaCodigoSituacao', models.BigIntegerField(primary_key=True, serialize=False)),
                ('SiglaSituacao', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TextoAssociado',
            fields=[
                ('CodigoTexto', models.BigIntegerField(primary_key=True, serialize=False)),
                ('DescricaoTipoTexto', models.TextField()),
                ('TipoDocumento', models.CharField(max_length=50)),
                ('FormatoTexto', models.CharField(max_length=200)),
                ('DataTexto', models.DateField()),
                ('UrlTexto', models.URLField()),
                ('DescricaoTexto', models.TextField()),
                ('AutoriaTexto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Providencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SiglaTipoProcedimento', models.CharField(max_length=100)),
                ('DescricaoTipoProcedimento', models.TextField()),
                ('NumOrdemProvidencia', models.IntegerField()),
                ('IndicadorReexame', models.CharField(max_length=50)),
                ('Destinatario', models.ManyToManyField(to='senado.Destinatario')),
            ],
        ),
        migrations.CreateModel(
            name='Prazo',
            fields=[
                ('CodigoTipoPrazo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('DescricaoTipoPrazo', models.TextField()),
                ('DescricaoTipoFundamento', models.TextField()),
                ('TipoFase', models.CharField(max_length=50)),
                ('DescricaoTipoFase', models.TextField()),
                ('IndicadorProrrogado', models.CharField(max_length=50)),
                ('DataInicioPrazo', models.DateField()),
                ('DataFimPrazo', models.DateField()),
                ('IdentificacaoComissao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='senado.identificacaocomissao')),
            ],
        ),
        migrations.CreateModel(
            name='Parlamentar',
            fields=[
                ('codigoParlamentar', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nomeParlamentar', models.TextField()),
                ('nomeCompletoParlamentar', models.TextField()),
                ('sexoParlamentar', models.CharField(max_length=20)),
                ('formaTratamento', models.CharField(max_length=50, null=True)),
                ('urlFotoParlamentar', models.URLField(null=True)),
                ('urlPaginaParlamentar', models.URLField(null=True)),
                ('emailParlamentar', models.EmailField(max_length=254, null=True)),
                ('siglaPartidoParlamentar', models.CharField(max_length=100, null=True)),
                ('ufParlamentar', models.CharField(max_length=10, null=True)),
                ('autoria', models.ManyToManyField(to='senado.Autoria')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemDoDia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataOrdemDoDia', models.DateField()),
                ('DescricaoTipoApreciacao', models.TextField()),
                ('DescricaoResultado', models.TextField()),
                ('SessaoPlenaria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='senado.sessaoplenaria')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('identificacaoProcesso', models.CharField(max_length=20, null=True)),
                ('descricaoIdentificacao', models.CharField(max_length=100, null=True)),
                ('sigla', models.CharField(max_length=10, null=True)),
                ('numero', models.CharField(max_length=10, null=True)),
                ('ano', models.CharField(max_length=4, null=True)),
                ('siglaComissao', models.CharField(max_length=20, null=True)),
                ('ementa', models.TextField(null=True)),
                ('autor', models.TextField(null=True)),
                ('data', models.DateField(null=True)),
                ('urlDetalheMateria', models.URLField(null=True)),
                ('OrigemMateria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='senado.origemmateria')),
                ('assunto', models.ManyToManyField(to='senado.Assunto')),
                ('autoria', models.ManyToManyField(to='senado.Autoria')),
                ('autuacao', models.ManyToManyField(to='senado.Autuacao')),
                ('classificacao', models.ManyToManyField(to='senado.Classificacao')),
                ('despacho', models.ManyToManyField(to='senado.Despacho')),
                ('emenda', models.ManyToManyField(to='senado.Emenda')),
                ('ordemDoDia', models.ManyToManyField(to='senado.OrdemDoDia')),
                ('prazo', models.ManyToManyField(to='senado.Prazo')),
            ],
        ),
        migrations.CreateModel(
            name='InformesLegislativo',
            fields=[
                ('Data', models.DateTimeField()),
                ('IdInformeLegislativo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CodigoTramitacaoLegado', models.BigIntegerField()),
                ('Descricao', models.TextField()),
                ('Local', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='senado.local')),
                ('SituacaoIniciada', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='senado.situacaoiniciada')),
                ('TextoAssociado', models.ManyToManyField(to='senado.TextoAssociado')),
            ],
        ),
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='senado.materia')),
            ],
        ),
        migrations.AddField(
            model_name='despacho',
            name='Providencia',
            field=models.ManyToManyField(to='senado.Providencia'),
        ),
        migrations.CreateModel(
            name='Decisao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('sigla', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='senado.materia')),
            ],
        ),
        migrations.CreateModel(
            name='DadosBasicosMateria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ementaMateria', models.TextField()),
                ('explicacaoEmentaMateria', models.TextField(null=True)),
                ('apelidoMateria', models.TextField(null=True)),
                ('casaIniciadoraNoLegislativo', models.CharField(max_length=50)),
                ('indicadorComplementar', models.CharField(max_length=50)),
                ('dataApresentacao', models.DateField()),
                ('dataLeitura', models.DateField(null=True)),
                ('siglaCasaLeitura', models.CharField(max_length=50, null=True)),
                ('NaturezaMateria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='senado.naturezamateria')),
                ('indexacaoMateria', models.ManyToManyField(to='senado.IndexacaoMateria')),
                ('materia', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='senado.materia')),
            ],
        ),
        migrations.AddField(
            model_name='autuacao',
            name='InformesLegislativo',
            field=models.ManyToManyField(to='senado.InformesLegislativo'),
        ),
        migrations.AddField(
            model_name='autuacao',
            name='SituacaoAtual',
            field=models.ManyToManyField(to='senado.SituacaoAtual'),
        ),
    ]
