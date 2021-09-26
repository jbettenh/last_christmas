from django.urls import path

from . import views
"""
   path('<int:movielist_id>/', views.detail, name='detail'),
   """
app_name = 'christmasflix'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:movielist_id>/add_movie/', views.add_movie, name='add_movie'),
    path('results/', views.results, name='results')
]
