from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:list_id>/', views.detail, name='detail'),
    path('<int:list_id>/results/', views.results, name='results'),
    path('<int:list_id>/vote/', views.vote, name='vote')
]
