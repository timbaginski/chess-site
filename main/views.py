from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .controllers import userController

# return signup page
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    email = request.POST.get('email', None)

    status = userController.createUser(username, password, email)

    if not status:
        return render(request, 'signup.html')
    
    return render(request, 'signup.html')


