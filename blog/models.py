from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
    )
    
    content = models.TextField(
        null = False,   
    )
    
    date_posted = models.DateTimeField(
        default=timezone.now,
        null=False,
    )
    
    author = models.ForeignKey(
        on_delete=models.CASCADE,
        to=User,
    )
    
    class  Meta:
        ordering = ['-date_posted']