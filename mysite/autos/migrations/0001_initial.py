# Generated by Django 3.1.1 on 2020-10-25 21:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese como (e. g Dofge))', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'En el nombre debes ingresar mas de un caracter')])),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'En el Nickname debes ingresar mas de un caracter')])),
                ('mileage', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=300)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.make')),
            ],
        ),
    ]