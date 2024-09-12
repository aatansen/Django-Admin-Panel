from django.contrib import admin
from .models import *

# Register your models here.

class Edu_admin_site(admin.AdminSite):
    site_header="Education Admin"
edu_site=Edu_admin_site(name='edu_site')
edu_site.register(Course_model)
edu_site.register(Lecture_model)

class Admin_login_area(admin.AdminSite):
    login_template='admin/login.html'

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
    # fields=('lecture_name','course','slug')
    fieldsets=(
        ('Lecture:',{
            'fields':('lecture_name','slug'),
            'description':'lecture details',
        }),
        ('Course:',{
            'fields':('course',),
            'description':'Course linked',
        }),
    )
    prepopulated_fields={
        'slug':('lecture_name',)
    }
admin.site.register(Lecture_model,Lecture_admin)
