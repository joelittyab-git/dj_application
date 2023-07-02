from django.db import models
from django.contrib.auth.models import AbstractUser
from .forms import RegValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )
    
    profile_picture = models.ImageField(
        upload_to='user_profile',
        editable=True,
    )
    
    bio = models.TextField(
        blank=True,
        editable=True,
    )
    
    def __str__(self) -> str:
        return self.user.username + "'s Profile"