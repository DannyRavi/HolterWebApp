from django.db import models
from datetime import datetime
from django.forms import ModelForm
from datetime import datetime
from holter.models import Profiles
# Create your models here.


class Docs(models.Model):

    user = models.ForeignKey(Profiles,related_name='docs',on_delete=models.CASCADE)
    data_date =  models.DateTimeField(default=datetime.now, blank=True)
    
    lead_1 = models.CharField(max_length=10000, blank=True, default='')
    lead_2 = models.CharField(max_length=10000, blank=True, default='')
    lead_3 = models.CharField(max_length=10000, blank=True, default='')
    lead_4 = models.CharField(max_length=10000, blank=True, default='')
    lead_5 = models.CharField(max_length=10000, blank=True, default='')
    lead_6 = models.CharField(max_length=10000, blank=True, default='')
    lead_7 = models.CharField(max_length=10000, blank=True, default='')
    lead_8 = models.CharField(max_length=10000, blank=True, default='')
    lead_9 = models.CharField(max_length=10000, blank=True, default='')
    lead_10 = models.CharField(max_length=10000, blank=True, default='')
    lead_11 = models.CharField(max_length=10000, blank=True, default='')
    lead_12 = models.CharField(max_length=10000, blank=True, default='')

    eject_button = models.BooleanField()

    

