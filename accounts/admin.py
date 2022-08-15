from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
# from .forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        ("Personal Info", {
            'fields': ('first_name', 'last_name', 'phone_number')
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)
