# Generated by Django 3.1 on 2020-09-24 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sqlserverconn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePrestador', models.CharField(max_length=500)),
                ('nombreEspecialidad', models.CharField(max_length=200)),
                ('direccionPrestador', models.CharField(max_length=200)),
                ('telefonoPrestador', models.CharField(max_length=20)),
                ('localidadPrestador', models.CharField(max_length=30)),
                ('provinciaPrestador', models.CharField(max_length=30)),
            ],
        ),
    ]