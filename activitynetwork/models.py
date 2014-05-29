from django.db import models

class Need(models.Model):
    description = models.CharField(max_length=30)
    def __str__(self):              # __unicode__ on Python 2
        return self.description

class Activity(models.Model):
    #act_holder = models.ForeignKey(MyProfile)
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    datetime = models.DateTimeField('activity date')
    description = models.CharField(max_length=30)
    needs = models.ManyToManyField(Need)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

