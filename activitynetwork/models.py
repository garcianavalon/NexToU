from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
from userena.models import UserenaBaseProfile 

class Activity(models.Models):
	act_holder = models.ForeignKey(MyProfile)
	act_name = models.CharField(max_length=30)
	act_place = models.CharField(max_length=30)   
	act_datetime = models.DateTimeField('activity date')
	#act_needs = models.CharField(max_length=30)
	act_description = models.CharField(max_length=30)  
