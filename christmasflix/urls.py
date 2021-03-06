from django.urls import path

from . import views

app_name = 'christmasflix'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.MovieListView.as_view(), name='movie_list'),
    path('new/', views.add_list, name='add_list'),
    path('delete/<int:list_id>', views.delete_list, name='delete_list'),
    path('<int:movielist_id>/add_movie/<str:movie_title>', views.add_movie, name='add_movie'),
    path('<int:movielist_id>/delete_movie/<int:movie_id>', views.delete_movie, name='delete_movie'),
    path('<int:movielist_id>/results/', views.show_results, name='show_results'),
    path('movies/', views.MoviesView.as_view(), name='movies'),
]
