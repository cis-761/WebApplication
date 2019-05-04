from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweets_list, name='tweets_list'),
]

