from django.db import models

# Create your models here.
class College(models.Model): 
    CollegeID = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=50) 
    strength = models.IntegerField() 
    website=models.URLField() 

    
class Principal(models.Model):
    CollegeID = models.OneToOneField(College,on_delete=models.CASCADE) 
    Qualification = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)   
    

class Teacher(models.Model):
    TeacherID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=150)
    Qualification = models.CharField(max_length=200)    
    email = models.EmailField(max_length=50)
    
    
class Subject(models.Model):
    subjectCode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    credits = models.IntegerField()
    Teacher = models.ManyToManyField(Teacher)
    
    