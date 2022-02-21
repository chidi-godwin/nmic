from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'full_name', 'is_active')
    list_display_links = ('email',)

admin.site.register(User, CustomUserAdmin)
