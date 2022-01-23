from urllib import request
from django.db import models

class RequestService(models.Model):
    Full_name = models.CharField(max_length=30)
    Phone_number=models.IntegerField()
    Email_address=models.EmailField()
    Message=models.TextField()