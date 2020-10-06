from django.db import models

# Create your models here.
class Crud(models.Model):
    nama = models.CharField(max_length=100)
    motto = models.TextField()