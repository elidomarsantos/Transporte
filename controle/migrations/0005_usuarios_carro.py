# Generated by Django 4.0.5 on 2022-12-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0004_alter_usuarios_identidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='carro',
            field=models.CharField(blank=True, choices=[('01', '01'), ('02', '02'), ('Outra Congregação', 'Outra Congregação')], max_length=60, null=True),
        ),
    ]