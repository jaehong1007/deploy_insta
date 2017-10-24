from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import SignUpForm
from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('추가 정보', {'fields': (
            'img_profile',
            'age',
            'user_type',
            'like_posts',
        )}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('추가 정보', {
            'fields': (
                'img_profile',
                'age',
                'user_type',
            )
        }),
    )
    add_form = SignUpForm

admin.site.register(User, UserAdmin)
