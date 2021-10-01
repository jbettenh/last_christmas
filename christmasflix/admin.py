from django.contrib import admin
from .models import MovieList, Movie


class MoviesInline(admin.StackedInline):
    model = Movie
    extra = 1


class MovieListAdmin(admin.ModelAdmin):
    """
     fieldsets = [
        ('General', {'fields': ['name']}),
        ]

    """

    list_display = ('name', 'created_date')
    inlines = [MoviesInline]

    list_filter = ['created_date']


admin.site.register(MovieList, MovieListAdmin)
admin.site.register(Movie)

