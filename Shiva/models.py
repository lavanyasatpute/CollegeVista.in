from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    conformpassword = models.CharField(max_length=255)

    