# Generated by Django 4.0.1 on 2022-02-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.CharField(default='link', max_length=200),
        ),
    ]