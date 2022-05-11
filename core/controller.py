from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 

class Login:
    def loginSubmit(self, request):
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            if username != '' and password != '':

                try:
                    user = authenticate(username = username, password = password)
                    if user:
                        login(request, user)
                        return True
                except:
                    return False

class Register:
    def registerSubmit (self, request):
          if request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            passw_confirm = request.POST.get('confirmPassw')

            if (not (User.objects.filter(username = username) or User.objects.filter(email = email))) and password == passw_confirm:

                try:
                    User.objects.create_user(username, email, password)
                    return True

                except:
                    return False

class Deletion:
    def deleteAcc(self, request):
         if request.POST:
            user = request.user
            user_to_del = User.objects.get(username = user)

            username = request.POST.get('username')
            password = request.POST.get('password')
            passw_confirm = request.POST.get('confirmPassw')

            if password == passw_confirm:
                check = authenticate(username = username, password = password)

                if check and (check == user_to_del):
                    try:
                        user_to_del.delete()
                        return True
                    except:
                        return False

                else:
                    return False
