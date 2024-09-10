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
    search_fields=('name',)
    list_display=['name','membership_plan','membership_active','unique_code']
    list_filter=["membership_plan"]
    # exclude=('unique_code',)
    '''fields=(
        ('name','membership_plan'),
        'membership_active',
    )'''
    # list_display_links=['name','unique_code','membership_plan']
    # list_editable=['membership_plan','unique_code']
    
    actions=('set_membership_to_active',)
    
    def set_membership_to_active(self,request,queryset):
        queryset.update(membership_active=True)
        self.message_user(request,'Membership activated successfully')
    set_membership_to_active.short_description='Mark to set membership active'
admin.site.register(Membership_model,Membership_admin)