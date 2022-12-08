from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User as uit_share_user
from .forms import (
    Signup_Form,
    UserChange_Form
)


@admin.register(uit_share_user)
class UserAdmin(UserAdmin):
    fieldsets = (
        ("User Identification", {
            "fields": ("id", "username", "email", "password",),
        }),
        ("User Profile", {
            "fields": ("name", "avatar_img", "bio",),
        }),
        ("Date & Time", {
            "fields": ("date_joined", "last_login",),
        }),
        ("User's Authorization", {
            "fields": ("is_active", "is_staff", "is_superuser",),
        }),
        ("User's Permissions", {
            "classes": ("collapse",),
            "fields": ("user_permissions", "groups",),
        }),
    )
    add_fieldsets = (
        ("User Identification", {
            "fields": ("name", "username", "email", "password1", "password2",),
        }),
    )
    list_display = (
        "id",
        "username",
        "email",
        "name",
        "is_staff",
        "is_active",
        "date_joined",
    )
    list_display_links = ("id", "username", "email",)
    list_filter = ()
    readonly_fields = ("id", "date_joined", "last_login",)
    ordering = ["-is_superuser", "-is_staff", "-date_joined", "username",]
    add_form = Signup_Form
    form = UserChange_Form