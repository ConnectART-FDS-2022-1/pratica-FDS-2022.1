from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 
from django.contrib import messages 
from core.controller import *


def index(request):
  return redirect('/login/')


def loginPage(request):
  return render(request, 'logintest.html')


def registerPage(request):
  return render(request, 'registertest.html')


@login_required(login_url='/login/')
def deletePage(request):
  return render(request, 'deleteacctest.html')


@login_required(login_url = '/login/')
def viewPersonalProfile(request):
  user = request.user
  user_info = User.objects.filter(username = user)
  return render(request, 'myprofile.html', {'user' : user_info})


def loginSubmit(request):
  if request.POST:
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username != '' and password != '': 
      loginObj = Login()
      logged = loginObj.loginSubmit(username, password, request)

      if logged:
        return redirect('/profile/edit/')

    messages.error(request, 'Algo deu errado, tente novamente!')
    return redirect('/login/')


def registerSubmit(request):
  if request.POST:
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    passw_confirm = request.POST.get('confirmPassw')

    if (not (User.objects.filter(username = username) or User.objects.filter(email = email))) and password == passw_confirm:
      registerObj = Register()
      registered = registerObj.registerSubmit(username, email, password)

      if registered:
        return redirect('/login/')

    messages.error(request, 'Algo deu errado, tente novamente!')
    return redirect('/register/')


@login_required(login_url = '/login/')
def submitLogout(request):
  logout(request)
  return redirect('/')


@login_required(login_url = '/login/')
def deleteAccount(request):
  if request.POST:
    user = request.user
    user_to_del = User.objects.get(username = user)

    username = request.POST.get('username')
    password = request.POST.get('password')
    passw_confirm = request.POST.get('confirmPassw')

    if password == passw_confirm:
      check = authenticate(username = username, password = password)

      if check and (check == user_to_del):
        deleteObj = Deletion()
        deleted = deleteObj.deleteAcc(user_to_del)

        if deleted:
          messages.success(request, 'User successfully deleted.')
          return redirect('/')

    messages.error(request, 'Couldn\'t delete user.')
    return redirect('/profile/edit/')
  