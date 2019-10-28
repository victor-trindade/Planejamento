# Generated by Django 2.2.6 on 2019-10-27 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coordinator', '0002_auto_20191027_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99, verbose_name='Nome da Loja')),
                ('id_sf', models.CharField(max_length=18, verbose_name='ID da loja')),
                ('visit_day', models.DateField(verbose_name='Dia da Visita')),
                ('check_in', models.TimeField(verbose_name='Hora da entrada')),
                ('check_out', models.TimeField(verbose_name='Hora da saída')),
                ('coordinator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coordinator.Coordinator', verbose_name='Coordenador')),
            ],
        ),
    ]
