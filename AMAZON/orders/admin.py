from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

    fields = (
        "product",
        "quantity",
        "price",
        "subtotal_display",
    )

    readonly_fields = (
        "subtotal_display",
    )

    def subtotal_display(self, obj):
        if not obj.pk:
            return "-"

        return obj.subtotal

    subtotal_display.short_description = "Subtotal"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "customer",
        "created_at",
        "payment_successful",
        "total_amount_display",
        "delivery_status_display",
    )

    list_filter = (
        "payment_successful",
        "created_at",
    )

    search_fields = (
        "id",
        "customer__name",
        "customer__email",
    )

    readonly_fields = (
        "created_at",
        "total_amount_display",
        "delivery_status_display",
    )

    fields = (
        "customer",
        "created_at",
        "payment_successful",
        "total_amount_display",
        "delivery_status_display",
    )

    inlines = (
        OrderItemInline,
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        return queryset.select_related(
            "customer",
        ).prefetch_related(
            "items__product",
        )

    @admin.display(
        description="Total Amount",
        ordering="items__price",
    )
    def total_amount_display(self, obj):
        return obj.total_amount

    @admin.display(
        description="Delivery Status",
    )
    def delivery_status_display(self, obj):
        return obj.delivery_status

