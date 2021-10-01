from django.contrib import admin
from .models import MovieList, Movie


class MoviesInline(admin.TabularInline):
    model = Movie
    extra = 1
    fieldsets = [
        ('Movies', {'fields': ['title']}),
        (None, {'fields': ['movielist']})
    ]


class MovieListAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': ['name']}),
        ('Date information', {'fields': ['created_date'], 'classes': ['collapse']}),
     ]

    list_display = ('name', 'created_date')
    inlines = [MoviesInline]

    list_filter = ['created_date']


admin.site.register(MovieList, MovieListAdmin)
admin.site.register(Movie)

