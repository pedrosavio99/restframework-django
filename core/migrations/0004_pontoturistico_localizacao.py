# Generated by Django 4.0.3 on 2022-03-18 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
        ('core', '0003_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='localizacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='localizacao.localizacao'),
            preserve_default=False,
        ),
    ]
