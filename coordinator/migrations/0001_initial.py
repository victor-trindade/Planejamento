# Generated by Django 2.2.6 on 2019-10-25 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coord_name', models.CharField(max_length=50)),
                ('coord_id', models.CharField(max_length=20)),
            ],
        ),
    ]
