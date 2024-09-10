from django.contrib import admin
from .models import *

# Register your models here.
class Inline_lecture(admin.StackedInline):
    model=Lecture_model
    # extra=2
    max_num=2

class Course_admin(admin.ModelAdmin):
    list_display=['course_title','course_description','Course_heading']
    
    def Course_heading(self,obj):
        return obj.course_title + " - " + obj.course_description
    
    inlines=[Inline_lecture]
    prepopulated_fields={
        'slug':('course_title',)
    }
admin.site.register(Course_model,Course_admin)

class Lecture_admin(admin.ModelAdmin):
    prepopulated_fields={
        'slug':('lecture_name',)
    }
admin.site.register(Lecture_model,Lecture_admin)
