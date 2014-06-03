from django.db import models

class Need(models.Model):
    description = models.CharField(max_length=30)
<<<<<<< HEAD
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


        
        
=======
    def __unicode__(self):              # __unicode__ on Python 2
        return self.description
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name
>>>>>>> 3deeebae5168469d98ce461d35f8f9851c8152eb

class Activity(models.Model):
    #act_holder = models.ForeignKey(MyProfile)
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    datetime = models.DateTimeField('activity date')
    description = models.CharField(max_length=30)
    needs = models.ManyToManyField(Need)
<<<<<<< HEAD
    schedule = models.ForeignKey(Schedule)
    category = models.ForeignKey(Category)
    def __str__(self):              # __unicode__ on Python 2
        return self.name



=======
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
>>>>>>> 3deeebae5168469d98ce461d35f8f9851c8152eb
