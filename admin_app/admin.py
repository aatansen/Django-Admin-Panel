from django.contrib import admin
from .models import *
from django.contrib.auth.models import User,Group

admin.site.unregister(User)
admin.site.unregister(Group)
# Register your models here.
# admin.site.register(Membership_model)


# Customizing admin titles
admin.site.site_header="Admin Panel"
admin.site.index_title='Admin'
admin.site.site_title='Panel Practice'

# @admin.register(Membership_model)
class Membership_admin(admin.ModelAdmin):
    exclude=('unique_code',)
    '''fields=(
        ('name','membership_plan'),
        'membership_active',
    )'''
admin.site.register(Membership_model,Membership_admin)