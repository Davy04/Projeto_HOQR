# Generated by Django 4.2.5 on 2023-09-22 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('cpf', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Remedio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remedio', models.CharField(max_length=50)),
                ('quantidade', models.CharField(max_length=50)),
                ('duracao', models.CharField(max_length=50)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
            ],
        ),
    ]