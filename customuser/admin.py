from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from customuser.forms import CustomUserCreationForm, CustomUserChangeForm
from customuser.models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['email', 'first_name', 'last_name', 'is_superuser']
    list_filter = ['is_superuser']
    fieldsets = [
        (None, {"fields": ['email', 'password']}),
        ('Personal Info', {'fields': ['first_name', 'last_name']}),
        ('Permissions', {'fields': ['is_staff', 'is_active', 'groups', 'user_permissions']})
    ]

    add_fieldsets = [
        (None, 
         {
             'classes':['wide'],
             'fields': ['email', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions']
         })
    ]

    search_fields = ['email']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)