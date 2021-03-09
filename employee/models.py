from django.db import models
from user.models import User


# Create your models here.


class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    dob = models.DateField(blank=True,null=True)
    manager = models.ForeignKey(to=User, on_delete=models.CASCADE)
    company = models.CharField(max_length=500)
    mobile = models.CharField(max_length=12,null = True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
