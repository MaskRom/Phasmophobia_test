from email.quoprimime import body_check
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from taggit.managers import TaggableManager 


class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)
    icon = models.ImageField(upload_to="user_icon", blank=True, null=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField(null=False, blank=False, max_length=255)
    tags = TaggableManager(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.user}'

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    target = models.ForeignKey(Post, on_delete = models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.user}'