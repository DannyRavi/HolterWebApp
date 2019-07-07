from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth.models import User

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MS', 'Ms.'),
]

HOLTER_HOURS = [
    ('24:00 H', '48:00 H'),
    ('48:00 H', '48:00 H'),
]

# Create your models here.


# Create your models here.
class Profiles(models.Model):

    # id = models.AutoField(null=True)
    # birth_day = models.DateTimeField(default=datetime.now, blank=True)
    group = models.CharField(max_length=30, blank=True, default='patients')

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nation_code = models.CharField(max_length=10, blank=True, default='1234567890')
    first_name = models.CharField(max_length=20, blank=True, default='')
    last_name = models.CharField(max_length=20, blank=True, default='')
    phone_number = models.CharField(max_length=11, blank=True, default='')
    mobile_number = models.CharField(max_length=11, blank=True, default='')
    age = models.CharField(max_length=3, blank=True, default='')
    height = models.CharField(max_length=3, blank=True, default='')
    weigth = models.CharField(max_length=3, blank=True, default='')
    address = models.CharField(max_length=120, blank=True, default='')
    postal_code = models.CharField(max_length=15, blank=True, default='')
    email = models.EmailField(max_length=70,blank=True, null= True)
    gender = models.CharField(max_length=3, choices=TITLE_CHOICES,default='MR')

    #patient information
    angina = models.BooleanField()
    history_of_mi = models.BooleanField()
    prior_cath = models.BooleanField()
    prior_cabg = models.BooleanField()
    smoking = models.BooleanField()
    diabetic = models.BooleanField()
    family_history = models.BooleanField()
    paec_maker = models.BooleanField()
    indications = models.CharField(max_length=120, blank=True, default='')
    medications = models.CharField(max_length=120, blank=True, default='')
    procedure_type = models.CharField(max_length=3, choices=HOLTER_HOURS,default='MR')
    referring_physician = models.CharField(max_length=30, blank=True, default='')
    notes = models.CharField(max_length=250, blank=True, default='')
    technicain_name = models.CharField(max_length=30, blank=True, default='')
    attending_phy = models.CharField(max_length=30, blank=True, default='')
    request_time_data = models.DateTimeField(default=datetime.now, blank=True)
    location = models.CharField(max_length=30, blank=True, default='')

    
    # my_field = models.BooleanField(default=True)
