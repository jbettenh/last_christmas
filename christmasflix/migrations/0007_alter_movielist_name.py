# Generated by Django 3.2.7 on 2021-09-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmasflix', '0006_rename_movies_movie_movielist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
    ]