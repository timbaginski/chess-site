from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# insert a new user into the db if request is valid
def createUser(username, password, email):
    if not username or not password or not email:
        return False
    
    if usernameExists(username):
        return False

    User.objects.create_user(username=username, password=password, email=email)

def usernameExists(username):
    return User.objects.filter(username=username).exists()

# sign in a user if username/password is valid
def loginUser(username, password):
    user = authenticate(username=username, password=password)

    if not user:
        user = authenticateEmail(email=username, password=password)

    return user


def authenticateEmail(email, password):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(email=email)
    except UserModel.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    
    return None
    




    

