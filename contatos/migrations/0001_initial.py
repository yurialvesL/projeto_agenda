# Generated by Django 4.0.4 on 2022-05-03 17:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(blank=True, max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('data_criacao', models.DateTimeField(default=datetime.datetime(2022, 5, 3, 17, 56, 51, 922980, tzinfo=utc))),
                ('descricao', models.CharField(blank=True, max_length=255)),
                ('categora', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contatos.categoria')),
            ],
        ),
    ]