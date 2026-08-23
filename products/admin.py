from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "price",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )
