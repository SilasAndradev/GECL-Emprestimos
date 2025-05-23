# Generated by Django 5.1.7 on 2025-04-27 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('moderator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('data_prevista', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('data_devolvida', models.DateTimeField(blank=True, null=True)),
                ('devolvido', models.BooleanField(default=False)),
                ('devolução_confirmada', models.BooleanField(default=False)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.aluno')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='moderator.material')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
