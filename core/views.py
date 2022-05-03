from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 
from django.contrib import messages 


def index(request):
  return redirect('/login/')


def loginPage(request):
  return render(request, 'login.html')


def loginSubmit(request):
  if request.POST:
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username != '' and password != '':

      try:
        user = authenticate(username = username, password = password)
        if user:
          login(request, user)
          return redirect('/profile/edit/')

      except:
        pass

    messages.error(request, 'Algo deu errado, tente novamente!')
    return redirect('/login/')


def registerPage(request):
  return render(request, 'register.html')


def registerSubmit(request):
  if request.POST:
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    passw_confirm = request.POST.get('confirmPassw')

    if (not (User.objects.filter(username = username) or User.objects.filter(email = email))) and password == passw_confirm:

      try:
        User.objects.create_user(username, email, password)
        return redirect('/login/')

      except:
        messages.error(request, 'Algo deu errado, tente novamente!')

  return redirect('/register/')


@login_required(login_url = '/login/')
def submitLogout(request):
  logout(request)
  return redirect('/')


@login_required(login_url = '/login/')
def deleteAccount(request):
  user = request.user
  user_to_del = User.objects.get(username = user)

  try:
    user_to_del.delete()
  except:
    messages.error('Couldn\'t delete user.')

  return redirect('/profile/edit/')

@login_required(login_url = '/login/')
def viewPersonalProfile(request):
  user = request.user
  user_info = User.objects.filter(username = user)
  return render(request, 'myprofile.html', {'user' : user_info})
  