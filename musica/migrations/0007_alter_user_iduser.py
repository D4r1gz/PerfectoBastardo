# Generated by Django 4.0.4 on 2022-06-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0006_alter_detallepedido_iddetalle_alter_pedido_idpedido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='iduser',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
