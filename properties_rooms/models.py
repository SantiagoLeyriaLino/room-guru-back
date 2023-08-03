from django.db import models
from users.models import CustomUser

# Create your models here.

class Property(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="properties")
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return (self.city + ' _ ' + self.address)



class Room(models.Model):
    room_number = models.CharField(max_length=10)
    property = models.ForeignKey(Property, on_delete=models.PROTECT, related_name='rooms')
    tenant = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='room', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return (self.room_number + '/' + self.property.address)