# Generated by Django 5.1.3 on 2024-11-07 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('tag', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]