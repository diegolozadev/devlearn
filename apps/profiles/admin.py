from django.contrib import admin
from .models import User, InstructorProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Rol personalizado', {'fields': ('is_instructor',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('', {'fields': ('is_instructor',)}),
    )

@admin.register(InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'website')
    search_fields = ('user__username', 'bio')