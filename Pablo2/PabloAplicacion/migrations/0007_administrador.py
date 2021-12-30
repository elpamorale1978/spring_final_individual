# Generated by Django 3.2.9 on 2021-11-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PabloAplicacion', '0006_usuario_last_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=70)),
                ('contrasena', models.CharField(max_length=30)),
                ('last_login', models.CharField(max_length=300)),
            ],
        ),
    ]