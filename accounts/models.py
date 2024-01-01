from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous', help_text='Required')
    email = models.EmailField(max_length=100, unique=True, help_text='Required')
    username = models.CharField(max_length=50, unique=True, help_text='Required')
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.email
    
