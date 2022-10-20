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



# inscription
def register(request):
    if request.method == "POST" :
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if User.objects.filter(username=username):
            messages.error(request, "Ce nom d'utilisateur est déjà utilisé.")
            return redirect('register')
        if User.objects.filter(email=email):
            messages.error(request, "Cette adresse email est déjà liée à un compte.")
            return redirect ('register')    
        if not username.isalnum():
            messages.error(request, "Le nom doit etre alphanumeric")
            return redirect ('register')    
        if password != password1 :
            messages.error(request, "Les deux mot de passe ne correspondent pas.")
            return redirect ('register')

        mon_utilisateur = User.objects.create_user(username, email, password)
        mon_utilisateur.first_name = firstname 
        mon_utilisateur.last_name = lastname
        mon_utilisateur.save()
        messages.success(request, 'Votre compte a été crée avec succes')
        return redirect('login')


    return render(request, 'app/register.html')

# connexion
def logIn(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
           login(request, user)
           firstname = user.first_name
           return render(request, 'app/index.html', {'firstname': firstname })
        else:
            messages.error(request, 'Mauvaise authentification') 
            return redirect('login')
    
    return render(request, 'app/login.html')

#déconnexion
def logOut(request):
    logout(request)
    messages.success(request, ' Vous avez été déconnecté')
    return redirect('home')
       
#newletters
def newsletter(request):
    
    return render(request, 'app/newsletter.html')

#statistique
def stats(request):
    
    return render(request, 'app/stats.html')

#accueil

def accueil(resquest):
    return render(resquest,'app/index.html')

#test
def test(resquest):
    return render(resquest,'app/test.html')

#DTU

def DTU(resquest):
    
    return render(resquest,'app/DTU.html')
