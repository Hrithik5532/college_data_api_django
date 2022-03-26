from __future__ import division
from pyexpat import model
from tkinter import CASCADE
from django.db import models


class Month(models.TextChoices):
    
        FirstYear="First Year"
        SecondYear="second Year"
        ThirdYear="third Year"
        FourYear="fourth Year"
# Create your models here.
class Branch(models.Model):
    branch = models.CharField(max_length=50)
    def __str__(self):
        return self.branch
class TeacherData(models.Model):
    #tid = models.AutoField(primary_key=True) 
    tname = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,related_name='teacher')
    clg_yr = models.CharField(max_length=20,choices=Month.choices,default=Month.FirstYear)
    def __str__(self):
        return self.tname

class  StudentData(models.Model):
    SId= models.AutoField(primary_key=True)
    teacher_name= models.ForeignKey(TeacherData,on_delete=models.CASCADE,related_name='student')
    sname=models.CharField(max_length=50)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,related_name='student')
    clg_yr = models.CharField(max_length=20,choices=Month.choices,default=Month.FirstYear)
    def __str__(self):
        return self.sname