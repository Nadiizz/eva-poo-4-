# Generated by Django 5.1.4 on 2024-12-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
                ('apodo', models.CharField(max_length=50)),
                ('edad', models.SmallIntegerField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]