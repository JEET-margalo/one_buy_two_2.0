# threeapp/models.py

from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15,null=True)
    account = models.CharField(max_length=255,null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name
   