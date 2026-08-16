from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="customer",
    )

    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
    )

    email = models.EmailField()

    mobile = models.CharField(
        max_length=20,
    )

    street = models.CharField(
        max_length=255,
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100,
    )

    postcode = models.CharField(
        max_length=20,
    )

    country = models.CharField(
        max_length=100,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return (
            f"{self.first_name} "
            f"{self.last_name}"
        )
