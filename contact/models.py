from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.TextField(max_length=50)
    email=models.EmailField(max_length=100)
    message=models.TextField(max_length=1000)

    