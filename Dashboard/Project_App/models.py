from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,validators=[MinLengthValidator(6)])