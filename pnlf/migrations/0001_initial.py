# Generated by Django 4.1.1 on 2022-09-19 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('modificado_el', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('no_jugadores', models.IntegerField()),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('modificado_el', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('modificado_el', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('modificado_el', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('fecha_nacimiento', models.DateField()),
                ('numero', models.IntegerField()),
                ('posicion', models.CharField(max_length=30)),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('modificado_el', models.DateTimeField(auto_now=True)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pnlf.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('capacidad', models.IntegerField()),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('modificado_el', models.DateTimeField(auto_now=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pnlf.ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='estadio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pnlf.estadio'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='liga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pnlf.liga'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pnlf.estado'),
        ),
    ]