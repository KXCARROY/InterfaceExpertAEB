from unicodedata import name
from django.urls import path
from app import views



urlpatterns = [
    path('', views.home, name="home"),
    path('newsletter', views.newsletter, name = 'newsletter'),
    path('stats', views.stats, name = 'stats'),
    path('accueil', views.accueil, name = 'accueil'),
    path('DTU', views.DTU, name = 'DTU'),
    ]