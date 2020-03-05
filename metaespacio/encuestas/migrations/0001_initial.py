# Generated by Django 2.2.11 on 2020-03-05 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField()),
                ('fecha_finalizacion', models.DateTimeField(blank=True, null=True)),
                ('pregunta', models.CharField(max_length=255)),
                ('texto', models.TextField(blank=True)),
                ('voto_anonimo', models.BooleanField()),
                ('voto_multiple', models.BooleanField()),
                ('voto_editable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eleccion', models.CharField(max_length=255)),
                ('texto', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
