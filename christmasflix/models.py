from django.db import models


class MovieList(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=200, default='')
    created_date = models.DateTimeField('date created', default="1900-01-01 06:00")

    list_filter = ['created_date']

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(default='')
    movielist = models.ForeignKey(MovieList, default=None, on_delete=models.CASCADE,)

    def __str__(self):
        return self.title
