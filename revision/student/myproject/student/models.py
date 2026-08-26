from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=50)   
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    department=models.ForeignKey(Department, on_delete=models.CASCADE, related_name="students")
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

     