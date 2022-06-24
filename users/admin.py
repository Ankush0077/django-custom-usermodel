from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# @admin.register(User)
# class User(admin.ModelAdmin):
#     list_display=['phone_number','date_joined','is_phone_verified']
    
class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('phone_number','date_joined')
    list_filter = ('phone_number','date_joined','is_phone_verified','is_active','is_staff')
    ordering = ('date_joined',)
    list_display = ('phone_number','date_joined','is_phone_verified','is_active','is_staff')
    fieldsets = (
        (None, {'fields' : ('phone_number','date_joined','is_phone_verified',)}),
        ('Permissions', {'fields' : ('is_staff','is_active',)}),
        ('Personal Information', {'fields' : ('current_otp',)}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('phone_number','current_otp','password1','password2','is_phone_verified','is_active','is_staff',),
        })
    )
    
admin.site.register(User,UserAdminConfig)