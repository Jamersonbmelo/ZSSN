# Generated by Django 4.2 on 2023-04-07 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sobreviventes', '0004_sobrevivente_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('votado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votos_recebidos', to='sobreviventes.sobrevivente')),
                ('votante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votos_dados', to='sobreviventes.sobrevivente')),
            ],
            options={
                'unique_together': {('votante', 'votado')},
            },
        ),
    ]
