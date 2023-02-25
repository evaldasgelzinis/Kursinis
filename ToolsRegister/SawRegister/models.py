from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class JobCenter(models.Model):
    name = models.CharField('Name', max_length=50, help_text = 'Select or create job center')

    def __str__(self):
        return self.name

class SawName(models.Model):
    name = models.CharField('SawName', max_length=50)

    def __str__(self):
        return self.name

class Saw(models.Model):
    name = models.ForeignKey(SawName, max_length=50, help_text='Išsirinkite pjūklą')
    date_changed = models.DateField(auto_now_add=True)
    cutting_lenght = models.IntegerField('Meters')
    shift = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    


