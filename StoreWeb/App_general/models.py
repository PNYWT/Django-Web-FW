from atexit import register
from datetime import datetime
import email
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Subscription(models.Model):
    STATUS_choices = [
        ('unapproved', 'Unapproved'),
        ('approved', 'Approved'),
        ('banned', 'Banned')
    ]

    name = models.CharField(max_length=60)
    email = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=15, choices=STATUS_choices, default='unapproved')
    registered_at = models.DateTimeField(auto_now_add=True)
    food_set = models.ManyToManyField('App_foods.FoodModel')