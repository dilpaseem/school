from django.db import models

# Create your models here.
class AddTeachers(models.Model):
    name = models.CharField( max_length = 100)
    phone  = models.IntegerField( max_length = 100)
    subject = models.CharField( max_length = 100)
    email = models.CharField( max_length = 100)
    address = models.CharField( max_length = 100)
