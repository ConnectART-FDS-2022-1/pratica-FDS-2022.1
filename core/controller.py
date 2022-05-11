from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 

class Login:

  def loginSubmit(self, username, password, req):
    user = authenticate(username = username, password = password)
    if user:
        login(req, user)
        return True

    return False


class Register:

  def registerSubmit(self, username, email, password):
    try:
      User.objects.create_user(username, email, password)
      return True
    
    except:
      return False


class Deletion:
  
  def deleteAcc(self, user):
    try:
      user.delete()
      return True

    except:
      return False
