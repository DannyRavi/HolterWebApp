from django.db import models
from django.forms import ModelForm

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MS', 'Ms.'),
]

# Create your models here.
class Profiles(models.Model):
    nation_code = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_day = models.DateTimeField()
    address = models.CharField(max_length=120)
    sex = models.CharField(max_length=3, choices=TITLE_CHOICES)
