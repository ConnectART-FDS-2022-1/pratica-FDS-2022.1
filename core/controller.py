from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 
from core.models import Post


class UserController:

  def loginUser(self, username, password, req):
    user = authenticate(username = username, password = password)
    if user:
        login(req, user)
        return True

    return False

  def createUser(self, username, email, password):
    try:
      User.objects.create_user(username, email, password)
      return True
    
    except:
      return False

  def deleteUser(self, user):
    try:
      user.delete()
      return True

    except:
      return False


class PostController:

  def createPost(self, title, body, req):
    try:
      Post.objects.create(title = title, body = body, created_by = req.user)
      return True

    except:
      return False

  def getAllPosts(self):
    posts = Post.objects.all().order_by('-date_created')
    return posts