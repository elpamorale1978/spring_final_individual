# Generated by Django 3.2.9 on 2021-11-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PabloAplicacion', '0003_usuario_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
