# Generated by Django 4.0.4 on 2022-05-24 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0002_evento_precio_alter_evento_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.IntegerField(null=True, verbose_name='Precio'),
        ),
    ]
