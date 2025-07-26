from django.db import models

# Create your models here.


class Account(models.Model):
    user = models.CharField(max_length=200)
    account_name = models.CharField(max_length=200)
    created = models.CharField(max_length=200)
