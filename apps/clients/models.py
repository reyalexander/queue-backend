from django.db import models

class Clients(models.Model):
    dni = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    registration_date = models.DateTimeField(auto_now_add=True)
