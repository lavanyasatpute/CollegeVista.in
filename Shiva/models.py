from django.db import models
#import uuid

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self):
        return str(self.id)
#my_instance = User()
#my_instance.save()   
