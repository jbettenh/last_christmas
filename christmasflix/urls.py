from django.urls import path

from . import views

app_name = 'christmasflix'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movielist_id>/', views.detail, name='detail'),
    path('results/', views.results, name='results')
]
