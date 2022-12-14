# Generated by Django 4.1.2 on 2022-10-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('descricao', models.TextField()),
                ('status', models.CharField(choices=[('A Confirmar', 'A Confirmar'), ('Confirmado', 'Confirmado'), ('Finalizado', 'Finalizado')], max_length=12)),
                ('pais', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'agendamento',
            },
        ),
    ]
