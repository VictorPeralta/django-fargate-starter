from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models import User



class UserAdmin(BaseUserAdmin):
    list_display = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password", "is_active")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser")}),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()
    list_filter = ()
    add_fieldsets = (
        (None, {"fields": ("email", "password", "is_active")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser")}),
    )


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
