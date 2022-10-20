from contextlib import redirect_stdout

from django.shortcuts import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import loader
from django.contrib.auth import views

# Create your views here.


def home(resquest):
    return render(resquest,'app/index.html')

#newletters
def newsletter(request):
    
    return render(request, 'app/newsletter.html')

#statistique
def stats(request):
    
    return render(request, 'app/stats.html')

#accueil

def accueil(resquest):
    return render(resquest,'app/index.html')


#DTU

def DTU(resquest):
    
    return render(resquest,'app/DTU.html')
