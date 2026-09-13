from django.urls import path

from . import views


urlpatterns = [
    path(
        "cart/",
        views.cart,
        name="cart",
    ),

    path(
        "",
        views.order_list,
        name="order_list",
    ),

    path(
        "detail/<int:pk>/",
        views.order_detail,
        name="order_detail",
        ),

    # path(
    #     "update/<int:pk>/",
    #     views.order_update,
    #     name="order_update",
    # ),

    # path(
    #     "delete/<int:pk>/",
    #     views.order_delete,
    #     name="order_delete",
    # ),
]

