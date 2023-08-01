from django.db import models
from users.models import CustomUser
from properties_rooms.models import Property, Room

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='tasks')
    created = models.DateTimeField(auto_now_add=True)
    date_to_be_made = models.DateField(null=True)
    dateCompleted= models.DateTimeField(null=True)   
    important = models.BooleanField(default=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='tasks', null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='tasks', null=True)

    def __str__(self):
        return (self.title)