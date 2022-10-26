from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class AdminLogin(models.Model):
    username = models.CharField( max_length = 100)
    password = models.CharField( max_length = 100)