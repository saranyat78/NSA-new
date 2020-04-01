from django.db import models

# Create your models here.


class Tech(models.Model):
    DeviceIP = models.CharField(max_length=100, editable=False)
    Account_Name = models.CharField(max_length=200)
    ConfigDifference = models.CharField(max_length=200, primary_key=True)


class Tech1(models.Model):
    DeviceIP = models.CharField(max_length=100)
    Account_Name = models.CharField(max_length=200, default='', editable=False)
    BWUtilization = models.CharField(max_length=200)
    Average = models.IntegerField(primary_key=True)
