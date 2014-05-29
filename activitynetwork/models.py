from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
from userena.models import UserenaBaseProfile 
  
class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
    							unique=True,
    							verbose_name=_('user'),
    							related_name='my_profile') 
    description = models.CharField(max_length=30)   
    resume = models.CharField(max_length=30) 
    #talents  = models.CharField(max_length=30)
    def __unicode__(self):
    	return user