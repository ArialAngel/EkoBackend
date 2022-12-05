from django.db import models

# Create your models here.

class DB_moochi(models.Model):
    username= models.CharField(max_length=20)
    nombre = models.CharField(max_length=101)
    apellido = models.CharField(max_length=101)
    email = models.EmailField()
    password1= models.CharField(max_length=10)
    password2= models.CharField(max_length=10)