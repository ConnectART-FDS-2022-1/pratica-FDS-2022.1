from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 
from core.models import Post


class UserController:

  def __checkExistingEmail(self, email):
    if User.objects.filter(email = email):
      return True

    else:
      return False


  def __checkExistingUsername(self, username):
    if User.objects.filter(username = username):
      return True

    else:
      return False


  def loginUser(self, username, password, req):
    user = authenticate(username = username, password = password)
    if user:
        login(req, user)
        return True

    return False


  def createUser(self, username, email, password):
    if not self.__checkExistingEmail(email) and not self.__checkExistingUsername(username):
      try:
        User.objects.create_user(username, email, password)
        return True
      
      except:
        return False

    else:
      return False


  def deleteUser(self, username, password, logged_user):
    user_to_del = authenticate(username = username, password = password)

    if user_to_del and (user_to_del == logged_user):
      try:
        user_to_del.delete()
        return True

      except:
        return False

    else:
      return False


class PostController:

  def createPost(self, title, body, user):
    try:
      Post.objects.create(title = title, body = body, created_by = user)
      return True

    except:
      return False


  def getAllPosts(self):
    posts = Post.objects.all().order_by('-date_created')
    return posts
