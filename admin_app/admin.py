from django.contrib import admin
from .models import *
from django.contrib.auth.models import User,Group

admin.site.unregister(User)
admin.site.unregister(Group)
# Register your models here.
# admin.site.register(Membership_model)

# @admin.register(Membership_model)
class Membership_admin(admin.ModelAdmin):
    pass
admin.site.register(Membership_model,Membership_admin)