from django.db import models

# Create your models here.
class College(models.Model): 
    CollegeID = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=50) 
    strength = models.IntegerField() 
    website=models.URLField() 

    def __str__(self):
        return f"{self.CollegeID} {self.name} has {self.strength} strength and can be view at {self.website}"
    
class Principal(models.Model):
    CollegeID = models.OneToOneField(College,on_delete=models.CASCADE) 
    Qualification = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)   
    
    def __str__(self):
        return f"{self.CollegeID} Principal has {self.Qualification} and can be reach out at {self.email}"

class Teacher(models.Model):
    TeacherID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=150)
    Qualification = models.CharField(max_length=200)    
    email = models.EmailField(max_length=50)
    
    def __str__(self):
        return f"{self.Name} having {self.Qualification} qualification, and can be reached at {self.email}"
    
class Subject(models.Model):
    subjectCode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    credits = models.IntegerField()
    Teacher = models.ManyToManyField(Teacher)
    
    def __str__(self):
        teacher_names = ", ".join([teacher.Name for teacher in self.Teacher.all()])
        return f"{self.name} has been assigned to {teacher_names if teacher_names else 'no teacher yet'}"
