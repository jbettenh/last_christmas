# Generated by Django 3.2.7 on 2021-10-09 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmasflix', '0010_movie_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.TextField(default='1900'),
        ),
    ]