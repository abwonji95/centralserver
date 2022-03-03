from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField, IntegerField
from django.db.models import Avg, Max, Min, Sum
from django.core.validators import MinValueValidator,MinLengthValidator
from django.contrib.auth.models import User,Group
from django.db.models.signals import post_delete, pre_save,post_save
import datetime
import uuid
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(User):

    email_verified = models.BooleanField(default=False)
    phone = models.CharField(max_length=20,null=True, blank=True, unique=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
  
    def __str__(self) :
        return "{} {}".format(self.first_name,self.last_name)

class Article(models.Model) :

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return "{} {}".format(self.title,self.author)

    