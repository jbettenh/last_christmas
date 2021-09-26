from django.urls import path

from . import views

app_name = 'christmasflix'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movielist_id>/', views.detail, name='detail'),
    path('<int:movielist_id>/add_movie/', views.add_movie, name='add_movie'),
    path('results/', views.results, name='results')
]
