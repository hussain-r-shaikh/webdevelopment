from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "email",
        "mobile",
        "city",
        "country",
        "created_at",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "mobile",
    )

    list_filter = (
        "city",
        "country",
        "created_at",
    )
