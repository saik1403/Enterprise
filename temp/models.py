from django.db import models

# Create your models here.

class temp(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)