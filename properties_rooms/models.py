from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return (self.city + ' _ ' + self.address)
    


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    tenant = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return (self.room_number + '/' + self.property.address)