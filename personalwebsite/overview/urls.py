from django.urls import path

from . import views

urlpatterns = [
    path('overview/', views.index, name='index'),
    path('', views.hello_world, name='hello_world'),
]