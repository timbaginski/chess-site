from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .controllers import userController
from django.contrib.auth import authenticate, login, logout


# return signup page
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', context={"error": 0})
    
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    email = request.POST.get('email', None)

    status = userController.createUser(username, password, email)

    if not status:
        return render(request, 'signup.html', context={"error": 1})
    
    return render(request, 'signin.html', context={"error": 0})


# def return login page
def signin(request):
    if request.method == "GET":
        return render(request, 'login.html', context={"error": 0})

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    user = userController.loginUser(username, password)
    if user != None:
        login(request, user)
        return index(request)

    return render(request, 'login.html', context={"error": 1})

def logoutUser(request):
    logout(request)
    return signin(request)

def index(request):
    return render(request, 'index.html')

def play(request):
    if(request.user.is_authenticated):
        return render(request, 'play.html')

    return signin(request)

def queue(request):
    if(request.user.is_authenticated):
        return render(request, 'game.html')

    return signin(request)

    

