from django.contrib.auth.models import User
from django.db import models

class item(models.Model):
    FirstName=models.CharField(max_length=10)
    LastName=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete = models.CASCADE)

class DBase(models.Model):
    FirstName=models.CharField(max_length=60)
    LastName=models.CharField(max_length=60)
    password=models.CharField(max_length=60)
    email=models.CharField(max_length=60)

    def __str__(self):
        return self.FirstName









