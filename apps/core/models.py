from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    meta = models.DecimalField(max_digits=10, decimal_places=2)


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


class Transaction(models.Model):
    INCOMING = "IN"
    OUTGOING = "OUT"

    TRANSACTION_TYPE_CHOICES = [
        (INCOMING, "Incoming"),
        (OUTGOING, "Outgoing"),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=TRANSACTION_TYPE_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    note = models.CharField(max_length=250, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
