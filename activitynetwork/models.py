from django.db import models

class Need(models.Model):
    description = models.CharField(max_length=30)
    def __str__(self):              # __unicode__ on Python 2

        return self.description
class Schedule(models.Model):
    datetime = models.DateTimeField('schedule datetime')
    description = models.CharField(max_length=30)
    def __str__(self):
        return self.description
        
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    def __str__(self):
        return self.name


        
        

class Activity(models.Model):
    #act_holder = models.ForeignKey(MyProfile)
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    datetime = models.DateTimeField('activity date')
    description = models.CharField(max_length=30)
    needs = models.ManyToManyField(Need)
    schedule = models.ForeignKey(Schedule)
    category = models.ForeignKey(Category)
    def __str__(self):              # __unicode__ on Python 2
        return self.name



