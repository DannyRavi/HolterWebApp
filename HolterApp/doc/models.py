from django.db import models
from datetime import datetime
from django.forms import ModelForm
from datetime import datetime
from holter.models import Profiles
# Create your models here.


class Docs(models.Model):
    attending_physician = models.CharField(max_length=100, blank=True, default='')
    admission_date =  models.DateTimeField(default=datetime.now, blank=True)
    date_of_discharge =  models.DateTimeField(default=datetime.now, blank=True)
    patient_history = models.TextField(max_length=1000, blank=True, default='')
    primary_dignosis = models.TextField(max_length=1000, blank=True, default='')
    final_dignosis = models.TextField(max_length=1000, blank=True, default='')
    medical_surgical_procedures = models.TextField(max_length=1000, blank=True, default='')
    cause_of_date = models.TextField(max_length=1000, blank=True, default='')
    patient_condition_discharge = models.TextField(max_length=1000, blank=True, default='')
    recommendtions_discharge = models.TextField(max_length=1000, blank=True, default='')
    author = models.ForeignKey(Profiles,related_name='docs',on_delete=models.CASCADE)

