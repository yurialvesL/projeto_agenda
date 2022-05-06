# Generated by Django 4.0.4 on 2022-05-06 15:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_contato_mostrar_alter_contato_data_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%M'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 15, 11, 7, 621269, tzinfo=utc)),
        ),
    ]