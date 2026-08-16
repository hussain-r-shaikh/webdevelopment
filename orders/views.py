from django.contrib import messages

from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from .forms import OrderForm
from .models import Order


def order_list(request):

    orders = Order.objects.select_related(
        "customer",
        "product",
    )

    return render(
        request,
        "orders/order_list.html",
        {
            "orders": orders,
        },
    )


def order_detail(
    request,
    pk,
):

    order = get_object_or_404(
        Order.objects.select_related(
            "customer",
            "product",
        ),
        pk=pk,
    )

    return render(
        request,
        "orders/order_detail.html",
        {
            "order": order,
        },
    )


def order_create(request):

    if request.method == "POST":

        form = OrderForm(
            request.POST,
        )

        if form.is_valid():

            order = form.save()

            messages.success(
                request,
                "Order created successfully.",
            )

            return redirect(
                "orders:order_detail",
                pk=order.pk,
            )

    else:

        form = OrderForm()

    return render(
        request,
        "orders/order_form.html",
        {
            "form": form,
            "page_title": "Create Order",
        },
    )


def order_update(
    request,
    pk,
):

    order = get_object_or_404(
        Order,
        pk=pk,
    )

    if request.method == "POST":

        form = OrderForm(
            request.POST,
            instance=order,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Order updated successfully.",
            )

            return redirect(
                "orders:order_detail",
                pk=order.pk,
            )

    else:

        form = OrderForm(
            instance=order,
        )

    return render(
        request,
        "orders/order_form.html",
        {
            "form": form,
            "order": order,
            "page_title": "Edit Order",
        },
    )


def order_delete(
    request,
    pk,
):

    order = get_object_or_404(
        Order,
        pk=pk,
    )

    if request.method == "POST":

        order.delete()

        messages.success(
            request,
            "Order deleted successfully.",
        )

        return redirect(
            "orders:order_list",
        )

    return render(
        request,
        "orders/order_confirm_delete.html",
        {
            "order": order,
        },
    )
