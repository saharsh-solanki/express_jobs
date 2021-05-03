from django.db import models

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    def __str__(self):
        return self.message