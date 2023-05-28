from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload_song, name='upload_song'),
    path('songs/', views.song_list, name='song_list'),
]
