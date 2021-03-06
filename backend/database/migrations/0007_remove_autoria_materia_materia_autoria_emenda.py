# Generated by Django 4.0.2 on 2022-03-02 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_alter_parlamentar_codigodeputadonacamara_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoria',
            name='materia',
        ),
        migrations.AddField(
            model_name='materia',
            name='autoria',
            field=models.ManyToManyField(to='database.Autoria'),
        ),
        migrations.CreateModel(
            name='Emenda',
            fields=[
                ('codigoEmenda', models.BigIntegerField(primary_key=True, serialize=False)),
                ('numeroEmenda', models.IntegerField()),
                ('dataApresentacao', models.DateField()),
                ('colegiadoApresentacao', models.CharField(max_length=100)),
                ('descricaoTurno', models.CharField(max_length=100)),
                ('descricaoTipoEmenda', models.CharField(max_length=100)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.materia')),
            ],
        ),
    ]
