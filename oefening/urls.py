from django.urls import path

from . import views

app_name = 'oefening'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'<int:number>/', views.test, name='test'),
    path(r'movies/', views.movies, name='movies'),
    path(r'songs/', views.song, name='song'),
    path(r'apike/', views.apike, name='apike'),

]
