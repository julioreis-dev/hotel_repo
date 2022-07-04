from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import User
from django.contrib import admin


@admin.register(User)
class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display = ['username', 'email']
    fieldsets = UserAdmin.fieldsets + (
        ("custom fields", {"fields": ("bio",)}),
    )
