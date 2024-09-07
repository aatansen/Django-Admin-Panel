from django.contrib import admin
from .models import *

# Register your models here.
# @admin.register(Membership_model)
class Membership_admin(admin.ModelAdmin):
    pass
admin.site.register(Membership_model,Membership_admin)