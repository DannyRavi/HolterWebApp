from django.db import models
from django.forms import ModelForm
from datetime import datetime

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MS', 'Ms.'),
]

# Create your models here.
class Profiles(models.Model):
    nation_code = models.CharField(max_length=10, blank=True, default='1234567890')
    phone_number = models.CharField(max_length=11, blank=True, default='')
    first_name = models.CharField(max_length=20, blank=True, default='')
    last_name = models.CharField(max_length=20, blank=True, default='')
    birth_day = models.DateTimeField(default=datetime.now, blank=True)
    address = models.CharField(max_length=120, blank=True, default='')
    sex = models.CharField(max_length=3, choices=TITLE_CHOICES,default='MR')
