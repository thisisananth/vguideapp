from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    pub_date = models.DateField('date',editable=False)
    user = models.ForeignKey(User,editable=False) 
    task1 = models.CharField(max_length=200,editable=False)
    schd_poms1 = models.PositiveIntegerField('Scheduled Poms',editable=False)
    used_poms1= models.PositiveIntegerField('Acutal Poms Used')
    completed1 = models.BooleanField('Complete')
    task2 = models.CharField(max_length=200,editable=False)
    schd_poms2 = models.PositiveIntegerField('Scheduled Poms',editable=False)
    used_poms2= models.PositiveIntegerField('Acutal Poms Used')
    completed2= models.BooleanField('Complete')
    task3 = models.CharField(max_length=200,editable=False)
    schd_poms3 = models.PositiveIntegerField('Scheduled Poms',editable=False)
    used_poms3= models.PositiveIntegerField('Acutal Poms Used')
    completed3 = models.BooleanField('Complete')
    
    class Meta:
        ordering = ['pub_date']
    def __unicode__(self):
        return self.task1+ " " + self.task2 + " " + self.task3 + " " + str(self.completed1) + " " + str(self.completed2) + " " + str(self.completed3)
