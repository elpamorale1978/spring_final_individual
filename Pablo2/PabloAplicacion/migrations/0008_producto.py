# Generated by Django 3.2.9 on 2021-12-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PabloAplicacion', '0007_administrador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
