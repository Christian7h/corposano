from django.db import models

# Create your models here.

class Hola(models.Model):
    title=models.CharField(max_length=200)
