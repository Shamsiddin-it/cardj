from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name

class Car(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    year = models.IntegerField()
    price = models.DecimalField( max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="static/images", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name
    
