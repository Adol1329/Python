from django.contrib import admin

# Register your models here.
from.models import Student,Department

admin.site.register(Student)
admin.site.register(Department)
from django.contrib import admin,messages
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models.query import QuerySet
from django.urls import path
from users.forms import UserAdminChangeForm, UserAdminCreationForm

# Register your models here.

admin.site.site_header = "Student Management"
admin.site.site_title = "Student Management"
admin.site.index_title = "Student Management"



User = get_user_model()


class UserAdmin(BaseUserAdmin, admin.ModelAdmin,):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.

    list_display = (
        "first_name",
        "last_name",
        "username",
        "phone_number",
        "user_type",
        "email",
        "is_active",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "user_type",
        "is_active",
   

    )
    fieldsets = (
        (None, {"fields": (
            "username",
            "email",
            "user_type",
            "password"
        )}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active", 'user_permissions',

                )
            },
        ),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "user_type",
            "is_active",
            "password1",
            "password2"
        )}),
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",

    )

    ordering = ("first_name",)
    filter_horizontal = ()
    actions = [
        "disable_users",
        "enable_users",
    ]
   

    def disable_users(self, request, queryset):
        queryset.update(is_active=False)

    def enable_users(self, request, queryset):
        queryset.update(is_active=True)



    def has_add_permission(self, request) -> bool:
      
        return True

    def get_urls(self):
        urls = super().get_urls()
        return urls

admin.site.register(User, UserAdmin)
