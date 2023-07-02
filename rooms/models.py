from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    admin = models.ForeignKey(
        to = User,
        editable=True,
        on_delete=models.CASCADE,
    )
    topic = models.CharField(
        max_length=100,
        blank=False,
        editable=False
    )
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    #participants
    created = models.DateTimeField(
        auto_now_add=True,
    )
    room_id = models.IntegerField(
        auto_created=True,
        primary_key=True,
        blank=False,
        null=False,
        unique=True,
        editable=False
    )
    
    def __str__(self) -> str:
        return self.name
    
class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    message = models.TextField() 
    updated = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    room = models.ForeignKey(
        to =Room,
        on_delete=models.CASCADE,
        
    )
    
    def __str__(self) -> str:
        return self.message
    
    
    
    