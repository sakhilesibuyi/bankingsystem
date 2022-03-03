from decimal import MAX_EMAX
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username=models.CharField(max_length=255, unique=True)
    email=models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class Branch(models.Model):
    branch_name = models.CharField(max_length=250)
    branch_code = models.CharField(max_length=250)
    def __str__(self):
        return self.branch_name

class Bank(models.Model):
    bank_name = models.CharField(max_length=250)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE, related_name="branch")

class ClientConsultant(models.Model):
    name = models.CharField(max_length=250)

class Client(models.Model):
    name = models.CharField(max_length=250)
    client_Address = models.CharField(max_length=250)

