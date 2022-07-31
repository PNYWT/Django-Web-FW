from django.db import models

# Create your models here.

class FoodModel(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    special_Price = models.IntegerField(null=True)
    is_Premium = models.BooleanField(default=False)
    end_Promotion = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True)