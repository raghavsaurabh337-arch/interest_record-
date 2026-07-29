from django.db import models
from django.utils import timezone 

# Create your models here.
class Home(models.Model):
     name=models.CharField(max_length=100)
     amount=models.IntegerField()
     interest_rate=models.IntegerField()
     date=models.DateTimeField(auto_now=True)
     def __str__(self):
          return self.name

     