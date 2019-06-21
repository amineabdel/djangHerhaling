from django.urls import path

from . import views

app_name = 'oefening'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'<int:line1>/<int:line2>/', views.nummerkes, name='nummerkes'),

]
