from django.db import models

class Need(models.Model):
    description = models.CharField(max_length=30)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.description
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class Activity(models.Model):
    #act_holder = models.ForeignKey(MyProfile)
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    datetime = models.DateTimeField('activity date')
    description = models.CharField(max_length=30)
    needs = models.ManyToManyField(Need)
    category = models.ManyToManyField(Category)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Schedule(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    datetime = models.DateTimeField('schedule date')
    activity = models.ForeignKey(Activity)
    def __unicode__(self):
        return self.name
