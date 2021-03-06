# Generated by Django 4.0.2 on 2022-02-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('identificacao_processo', models.BigIntegerField()),
                ('descricao_identificacao', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=10)),
                ('numero', models.BigIntegerField()),
                ('ano', models.CharField(max_length=4)),
                ('ementa', models.TextField()),
                ('autor', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=15)),
                ('url_detalhe_materia', models.URLField()),
            ],
        ),
    ]
