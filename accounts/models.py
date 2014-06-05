from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from activitynetwork.models import Activity

class VolunteerProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='volunteer_profile')
    intro = models.CharField(_('intro'),
                                max_length=140)
    resume = models.CharField(_('resume'),
                                max_length=1000)
    talents = models.CharField(_('talents'),
                                max_length=300)

    participated_activities = models.ManyToManyField(Activity)
