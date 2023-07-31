from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    plan_type = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="transactions")
    payment_date = models.DateTimeField(auto_now_add=True)
    invoice = models.URLField(max_length=100)

    def __str__(self):
        return (self.plane + ' - ' + self.user.username)