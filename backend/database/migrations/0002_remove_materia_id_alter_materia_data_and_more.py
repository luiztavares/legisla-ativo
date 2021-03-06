# Generated by Django 4.0.2 on 2022-02-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='id',
        ),
        migrations.AlterField(
            model_name='materia',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='materia',
            name='ementa',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='materia',
            name='identificacao_processo',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='materia',
            name='numero',
            field=models.CharField(max_length=20),
        ),
    ]
