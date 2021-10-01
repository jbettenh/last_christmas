# Generated by Django 3.2.7 on 2021-10-01 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmasflix', '0007_alter_movielist_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielist',
            name='created_date',
            field=models.DateTimeField(default='1900-01-01 06:00', verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='movielist',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]