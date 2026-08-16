from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from django.urls import include, path


urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),


    path(
        "customers/",
        include("customers.urls"),
    ),

    path(
        "products/",
        include("products.urls"),
    ),

    path(
        "orders/",
        include("orders.urls"),
    ),

    path(
        "payments/",
        include("payments.urls"),
    ),
]


# ============================================================
# DEVELOPMENT STATIC / MEDIA SERVING
# ============================================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
