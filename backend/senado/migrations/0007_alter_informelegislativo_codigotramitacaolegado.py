# Generated by Django 3.2.16 on 2022-10-10 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senado', '0006_rename_situacaoiniciadacodigosituacao_situacaoiniciada_codigosituacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informelegislativo',
            name='CodigoTramitacaoLegado',
            field=models.BigIntegerField(null=True),
        ),
    ]
