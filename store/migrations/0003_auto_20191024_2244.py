# Generated by Django 2.2.6 on 2019-10-25 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_store_coord_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='coord_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coordinator.Coordinator', verbose_name='Coordenador'),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_id',
            field=models.CharField(max_length=20, verbose_name='ID da LOJA'),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_name',
            field=models.CharField(max_length=99, verbose_name='Nome da loja'),
        ),
    ]