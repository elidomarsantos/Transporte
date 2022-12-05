# Generated by Django 4.0.5 on 2022-12-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gerais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('congregação', models.CharField(blank=True, max_length=60, null=True)),
                ('cidade', models.CharField(blank=True, max_length=60, null=True)),
                ('estado', models.CharField(blank=True, max_length=60, null=True)),
                ('data_do_evento', models.DateField(blank=True, null=True)),
                ('valor_da_passagem', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantidade_de_ônibus', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(blank=True, null=True)),
                ('nome', models.CharField(blank=True, max_length=60, null=True)),
                ('identidade', models.IntegerField(blank=True, null=True)),
                ('telefone', models.CharField(blank=True, max_length=12, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('observações', models.CharField(blank=True, max_length=200, null=True)),
                ('quitado', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=30, null=True)),
                ('poltrona', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]
