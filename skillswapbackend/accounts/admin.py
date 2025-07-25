from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User , ProfileDetails

# Define a custom UserAdmin
class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin list view
    list_display = ('email', 'first_name', 'last_name', 'phone', 'is_staff')
    list_filter = ('is_staff', 'is_active', 'is_admin')
    # Field to search
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    # Field to order by
    ordering = ('email',)
    # Remove filter_horizontal since groups and user_permissions are not defined
    filter_horizontal = ()

    # Form fields for add/change user
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser')}),
    )
    # Fields for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'is_staff', 'is_active', 'is_admin', 'is_superuser')}
        ),
    )

# Register the custom UserAdmin with your User model
admin.site.register(User, CustomUserAdmin)
admin.site.register(ProfileDetails)
