# Generated by Django 3.2.16 on 2022-10-10 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('senado', '0005_auto_20221010_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='situacaoiniciada',
            old_name='SituacaoIniciadaCodigoSituacao',
            new_name='CodigoSituacao',
        ),
    ]