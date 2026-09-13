from datetime import timedelta

from django.db import models
from django.utils import timezone

from customers.models import Customer


class Order(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="orders",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    payment_successful = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order #{self.id}"

    @property
    def total_amount(self):
        return sum(
            item.subtotal
            for item in self.items.all()
        )

    @property
    def delivery_status(self):

        elapsed = timezone.now() - self.created_at

        if elapsed < timedelta(minutes=5):
            return "Confirmed"

        elif elapsed < timedelta(minutes=10):
            return "Processing"

        elif elapsed < timedelta(minutes=15):
            return "Shipped"

        elif elapsed < timedelta(minutes=30):
            return "Out for Delivery"

        return "Delivered"


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.PROTECT,
        related_name="order_items",
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"

    @property
    def subtotal(self):
        return self.price * self.quantity