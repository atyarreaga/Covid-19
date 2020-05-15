# Generated by Django 3.0.6 on 2020-05-14 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Covid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('country', models.CharField(max_length=30)),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'MASCULINO'), (2, 'FEMENINO')])),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'ENFERMOS'), (2, 'RECUPERADOS'), (3, 'FALLECIDOS')])),
            ],
        ),
    ]
