from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Machine_Info(models.Model):
    __tablename__ = 'machine_info'
    id = models.IntegerField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    zone = models.CharField(max_length=100)
    tenworldid = models.CharField(max_length=100)
    localip = models.CharField(max_length=120)
    interip = models.CharField(max_length=120)
