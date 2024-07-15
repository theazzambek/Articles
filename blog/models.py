from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_author = models.BooleanField(default=False)

class Articles(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_public = models.BooleanField(default=True)
    author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
