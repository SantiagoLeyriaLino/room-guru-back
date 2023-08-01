from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.PositiveBigIntegerField(null=True)
    contract = models.URLField(max_length=200, null=True)
    rent_payment_date = models.DateField(null=True)
    debtor = models.BooleanField(default=False)
    contract_end_date = models.DateField(null=True)
    plan_type = models.CharField(max_length=20, null=True)