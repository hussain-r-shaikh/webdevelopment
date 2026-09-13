from django.db import models




class Product(models.Model):

    CATEGORY_CHOICES = (
        ("Electronics", "Electronics"),
        ("Mobiles", "Mobiles"),
        ("Fashion", "Fashion"),
        ("Home", "Home"),
        ("Other", "Other"),
    )


    name = models.CharField(
        max_length=200,
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    
    description = models.TextField(
        blank=True,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
    )

    is_available = models.BooleanField(
        default=True,
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
        return self.name