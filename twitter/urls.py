from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweets_list, name='tweets_list'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('results/', views.results, name='results'),
]

