# Generated by Django 4.0.4 on 2022-05-18 16:02
# Generated by Django 4.0.4 on 2022-05-11 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('idtipo_Usu', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('tipoUsu', models.CharField(max_length=50, verbose_name='tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreUsuario', models.CharField(max_length=50, verbose_name='nombre')),
                ('Contrasenna', models.CharField(max_length=6, verbose_name='contrasenna')),
                ('Fecha_nac', models.DateField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.tipousuario')),
            ],
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('idEvento', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Evento')),
                ('nombreTipoEvento', models.CharField(max_length=60, verbose_name='Nombre Tipo de Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('nombreEvento', models.CharField(max_length=60, primary_key=True, serialize=False, verbose_name='Nombre Evento')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('fecha', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.tipoevento')),
            ],
        ),

    ]
