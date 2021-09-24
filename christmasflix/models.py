from django.db import models


class MovieList(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='')


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(default='')
    movies = models.ForeignKey(MovieList, default=None, on_delete=models.CASCADE,)
