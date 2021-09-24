from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movies_id>/', views.detail, name='detail'),
    path('<int:movies_id>/results/', views.results, name='results'),
    path('<int:movies_id>/vote/', views.vote, name='vote')
]
