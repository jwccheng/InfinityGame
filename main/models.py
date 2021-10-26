from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model as user_model
from django.db.models import F, Sum
from account.models import Account
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 
from uuid import uuid4

transactionMode = [
    ('IN','IN'), 
    ('OUT','OUT'), 
]

walletType = [
    ("Diamond", "Diamond"),
    ("Gold", "Gold"),
    ("Ruby", "Ruby"),
]

transactionCategory = [
    ("WITHDRAWAL", "WITHDRAWAL"),
    ("TRANSFER", "TRANSFER"),
    ("LUCKY", "LUCKY"),
    ("COMMISSION", "COMMISSION"),
    ("TOP-UP", "TOP-UP"),
    ("REGISTRATION", "REGISTRATION"),
    ("CONVERT", "CONVERT"),
]

User = user_model()

def generateUUID():
    return str(uuid4())

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)


class History(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    associate = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=transactionCategory)
    wallet = models.CharField(max_length=20, choices=walletType)
    mode = models.CharField(max_length=10, choices=transactionMode)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=3)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.member)

class LuckyNumberOrders(models.Model):
    order_id = models.CharField(max_length=200)
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=3)
    date_created = models.DateTimeField(default=timezone.now)

class LuckyNumber(models.Model):
    order = models.ForeignKey(LuckyNumberOrders, on_delete=models.CASCADE, null=True, related_name='ticket')
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    number = models.CharField(max_length=200)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=3)
    date_created = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return str(self.member) + ", " + str(self.date_created)


class WinningNumber(models.Model):
    first_prize = models.CharField(max_length=200)
    second_prize = models.CharField(max_length=200)
    third_prize = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.date_created)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=3)
    quantity = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.date_created)

class Redeem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=3)
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.date_created)

class TopUp(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=3)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.date_created)

class Convert(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=3)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.date_created)



