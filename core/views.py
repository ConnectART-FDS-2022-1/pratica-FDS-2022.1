from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 
from django.contrib import messages 
from controller import *


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
  loginObj = Login
  logged = loginObj.loginSubmit(request)

  if logged:
    return redirect('/profile/edit/')

  else:
    messages.error(request, 'Algo deu errado, tente novamente!')
    return redirect('/login/')


def registerSubmit(request):
  registerObj = Register
  registered = registerObj.registerSubmit(request)
  if registered:
    return redirect('/login/')
  else:
    messages.error(request, 'Algo deu errado, tente novamente!')
    return redirect('/register/')


@login_required(login_url = '/login/')
def submitLogout(request):
  logout(request)
  return redirect('/')


@login_required(login_url = '/login/')
def deleteAccount(request):
  deletedObj = Deletion
  deleted = deletedObj.deleteAcc(request)
  if deleted:
    messages.success(request, 'User successfully deleted.')
    return redirect('/')
  else:
    messages.error(request, 'Couldn\'t delete user.')
    return redirect('/profile/edit/')
  