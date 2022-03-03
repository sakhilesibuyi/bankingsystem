from decimal import MAX_EMAX
from pyexpat import model
from statistics import mode
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
    def __str__(self):
        return "{} - {}".format(self.bank_name, self.branch)

class ClientConsultant(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=250)
    client_Address = models.CharField(max_length=250)
    def __str__(self):
        return self.name
class AccountType(models.Model):
    type = models.CharField(max_length=250)

class Account(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="account_owner")
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE, related_name="acc_type")
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="bank")
    balance = models.FloatField(default=0.0)
    def save(self, *args, **kwargs):
        acc_type = AccountType.objects.filter(id=self.account_type)
        print(acc_type)

    def __str__(self):
        return "{} - {} - {}".format(self.owner, self.bank, self.account_type)

class Transfer(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="acc")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="trans_branch")

class Deposit(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class Withdrawal(models.Model):
    amount = models.FloatField(null=True,blank=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)