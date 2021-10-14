from django.urls import path

from . import views

app_name = 'christmasflix'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.add_list, name='add_list'),
    path('delete/<int:list_id>', views.delete_list, name='delete_list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:movielist_id>/add_movie/', views.add_movie, name='add_movie'),
    path('delete_movie/<int:movie_id>', views.delete_movie, name='delete_movie'),
    path('movies/', views.MoviesView.as_view(), name='movies'),
]
