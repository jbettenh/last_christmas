# Generated by Django 3.2.7 on 2021-09-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmasflix', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
