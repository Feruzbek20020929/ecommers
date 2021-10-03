from django.db import models


# Create your models here.
class adminmodel(models.Model):
    username=models.CharField(max_length=15)
    password = models.CharField(max_length=15)