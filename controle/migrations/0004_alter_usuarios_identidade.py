# Generated by Django 4.0.5 on 2022-12-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0003_gerais_assistente_gerais_coordenador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='identidade',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
