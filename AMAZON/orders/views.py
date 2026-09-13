import json
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from products.models import Product
from .models import Order
from .models import OrderItem
from .forms import OrderForm
from .models import Order, OrderItem
from products.models import Product
from django.contrib.auth.decorators import login_required



def cart(request):
    # -----------------------------------------
    # GET
    # -----------------------------------------
    if request.method == "GET":
        return render(
            request,
            "cart.html",
        )
    # -----------------------------------------
    # POST
    # Process checkout
    # -----------------------------------------
    if request.method == "POST":
        # User must login before checkout
        if not request.user.is_authenticated:
            return JsonResponse(
                {
                "message":
                    "Please login before checkout.",
                "login_url":
                    f"{reverse('login')}?next=/orders/cart/",
                },
                status=401,
            )
        # Get Customer from request.user
        try:
            customer = request.user.customer
        except AttributeError:
            return JsonResponse(
                {
                    "message":
                    "Customer profile not found."
                },
                status=400,
            )
        # Read AJAX JSON
        try:
            data = json.loads(
                request.body
            )
            items = data.get(
                "items",
                []
            )
        except json.JSONDecodeError:
            return JsonResponse(
                {
                    "message":
                        "Invalid cart data."
                },
                status=400,
            )
        if not items:
            return JsonResponse(
                {
                    "message":
                        "Cart is empty."
                },
                status=400,
            )
        try:
            with transaction.atomic():
                # -----------------------------
                # Create Order
                # -----------------------------
                order = Order.objects.create(
                    customer=customer,
                    payment_successful=True,
                )
                # -----------------------------
                # Create OrderItems
                # -----------------------------
                for item in items:
                    product_id = item["product_id"]
                    quantity = int(
                        item["quantity"]
                    )
                    if quantity < 1:
                        raise ValueError()
                    product = Product.objects.get(
                        id=product_id,
                        is_available=True,
                    )
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        # IMPORTANT:
                        # Never trust localStorage price
                        price=product.price,
                    )
        except Product.DoesNotExist:
            return JsonResponse(
                {
                    "message":"A product is unavailable."
                },
                status=400,
            )
        except (
            KeyError,
            TypeError,
            ValueError,
        ):
            return JsonResponse(
                {
                    "message":
                        "Invalid cart item."
                },
                status=400,
            )
        # -----------------------------------------
        # Checkout successful
        # -----------------------------------------
        return JsonResponse(
            {
                "success": True,
                "order_id": order.id,
                "redirect_url": reverse(
                    "order_detail",
                    kwargs={
                        "pk": order.id
                    },
                ),
            }
        )




@login_required
def order_detail(request, pk):

    order = get_object_or_404(
        Order,
        pk=pk,
        customer=request.user.customer,
    )

    return render(
        request,
        "success.html",
        {
            "order": order,
        },
    )


@login_required
def order_list(request):
    orders = Order.objects.filter(customer__user = request.user)
    return render(request, "orders/order_list.html", {"orders":orders})
