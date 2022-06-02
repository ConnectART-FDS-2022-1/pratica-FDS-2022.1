from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 
from django.contrib import messages
from core.models import Post, Profile
from core.controller import UserController, PostController


def index(request):
  return redirect('/login/')

#testar
def viewProfiles(request):
  profiles = Profile.objects.all()
  return render(request, 'profiles.html', { 
    'profiles': profiles
  })


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
      userObj = UserController()
      logged = userObj.loginUser(username, password, request)

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
    
    if password == passw_confirm:
      userObj = UserController()
      registered = userObj.createUser(username, email, password)

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
    username = request.POST.get('username')
    password = request.POST.get('password')
    passw_confirm = request.POST.get('confirmPassw')

    logged_user = request.user

    if password == passw_confirm:

      userObj = UserController()
      deleted = userObj.deleteUser(username, password, logged_user)

      if deleted:
        messages.success(request, 'User successfully deleted.')
        return redirect('/')

    messages.error(request, 'Couldn\'t delete user.')
    return redirect('/profile/edit/')


@login_required(login_url='/login/')
def feedPage(request):
  postObj = PostController()
  posts = postObj.getAllPosts()

  return render(request, 'feedtest.html', {'posts': posts})


@login_required(login_url='/login/')
def createPostPage(request):
  return render(request, 'createposttest.html')
  

@login_required(login_url='/login/')
def createPostSubmit(request):
  if request.POST:
    title = request.POST.get('title')
    body = request.POST.get('body')

    user = request.user

    postObj = PostController()
    posted = postObj.createPost(title, body, user)

    if not posted:
      messages.error(request, 'Houve um erro ao fazer sua postagem.')

  return redirect('/feed/')