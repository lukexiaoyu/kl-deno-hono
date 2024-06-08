from django.db import models

# Create your models here.
class Peo(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    sex=models.CharField(max_length=10)