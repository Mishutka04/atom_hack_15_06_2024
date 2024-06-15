from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no mobile field."""

    fieldsets = (
        (None, {'fields': (
            'email', 'mobile', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups',
                                      'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'mobile', 'password1', 'password2'),
        }),
    )
    list_display = (
        'email', 'mobile', 'first_name', 'last_name', 'is_staff',)
    search_fields = (
        'email', 'mobile', 'first_name', 'last_name')
    ordering = ('email', 'mobile',)
