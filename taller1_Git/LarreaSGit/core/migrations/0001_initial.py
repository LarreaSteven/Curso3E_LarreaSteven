# Generated by Django 4.1 on 2022-08-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LarreaMuñozGit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.TextField()),
                ('nombres', models.TextField()),
                ('apellidos', models.TextField()),
                ('profesor', models.FloatField()),
            ],
        ),
    ]
