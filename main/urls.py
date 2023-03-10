from django.urls import path
from . import views 

urlpatterns = [
    path('signup', views.signup),
    path('login', views.signin),
    path('logout', views.logoutUser),
    path('', views.index),
    path('play', views.play),
    path('queue', views.queue)
]