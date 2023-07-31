from django.db import models
from django.contrib.auth.models import User
from properties_rooms.models import Room

# Create your models here.

class Message(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.PROTECT, related_name='messages')
    message = models.TextField()
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return (self.tenant + ' - ' + self.room_number.room_number)