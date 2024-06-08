from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    color=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    year=models.IntegerField()
    description=models.CharField(max_length=100)
    