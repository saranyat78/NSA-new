from django.db import models


class ConfigDiff(models.Model):
    Device_1 = models.CharField(max_length=100)
    Device_2 = models.CharField(max_length=200)




