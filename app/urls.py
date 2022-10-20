from unicodedata import name
from django.urls import path
from app import views



urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name='register'),
    path('login', views.logIn, name='login'),
    path('logout', views.logOut, name = 'logout'),
    path('newsletter', views.newsletter, name = 'newsletter'),
    path('stats', views.stats, name = 'stats'),
    path('accueil', views.accueil, name = 'accueil'),
    path('test', views.test, name = 'test'),
    path('DTU', views.DTU, name = 'DTU'),
    ]