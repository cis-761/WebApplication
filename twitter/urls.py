from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.tweets_list, name='tweets_list'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('results/', views.results, name='results'),
    path('mongo_results/', views.mongo_results, name='mongo_results'),
    path('t-sne-cluster/', views.t_cluster, name='t_cluster'),
    path('intertopic-distance-map/', views.idm, name='idm'), 
    path('graphs/', views.graphs, name='graphs'), 
    path('postgresql/', views.postgresql, name='postgresql'), 
]

normalpatterns = [
        url(r'^login/', auth_views.LoginView,{'template_name': 'login.html'}, name ='login'),
         url(r'^register/', views.register,name ='register' ),
         url(r'^search/$', views.search, name='search'),
         url(r'^tweet_search/$', views.tweet_search, name='tweet_search'),
         url(r'^mongo/$', views.mongo, name='mongo'),
]

urlpatterns += normalpatterns

