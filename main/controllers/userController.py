from django.contrib.auth.models import User

def createUser(username, password, email):
    if not username or not password or not email:
        return False
    
    if usernameExists(username):
        return False

    User.objects.create_user(username=username, password=password, email=email)

def usernameExists(username):
    return User.objects.filter(username=username).exists()