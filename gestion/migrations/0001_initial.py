# Generated by Django 5.0.1 on 2024-01-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('cedula', models.IntegerField()),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
