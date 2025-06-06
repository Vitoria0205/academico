# Generated by Django 5.2.1 on 2025-05-26 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_disciplina_curso_alter_pessoa_turma'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='periodo',
            field=models.CharField(default=1, max_length=100, verbose_name='Periodo'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.curso'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='turma',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.turma'),
        ),
    ]
