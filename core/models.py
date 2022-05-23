from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  belongs = models.ForeignKey(User, on_delete=models.CASCADE)
  bio = models.TextField()

  class Meta:
    db_table = 'Profile'


class Post(models.Model):
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now=True)
  title = models.CharField(null=False, max_length=100, default='Post title')
  body = models.TextField(null=False)

  class Meta:
    db_table = 'Post'
