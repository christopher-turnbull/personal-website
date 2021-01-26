from django.urls import path

from . import views

urlpatterns = [
    path('swahili', views.mambo_dunia, name='mambo_dunia'),
]