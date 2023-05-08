from django.db import models

# Create your models here.
class Contact(models.Model):
    Caste = models.CharField(max_length=10)
    Percentile = models.IntegerField()
    Gender = models.CharField(max_length=10)