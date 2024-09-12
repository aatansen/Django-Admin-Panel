from django.db import models

# Create your models here.
class Course_model(models.Model):
    course_title=models.CharField(max_length=100)
    course_description=models.TextField(max_length=100)
    slug=models.SlugField(max_length=100)
    
class Lecture_model(models.Model):
    lecture_name=models.CharField(max_length=100)
    course=models.ForeignKey(Course_model,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=100)
    