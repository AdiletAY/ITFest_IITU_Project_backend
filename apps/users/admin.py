from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Additional Info",
            {
                "fields": (
                    "patronymic",
                    "course_number",
                    "iin",
                    "gpa",
                    "role",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
