from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,unique=True)
    city = models.CharField(max_length=30)


