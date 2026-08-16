from django.contrib import messages

from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from .forms import CustomerForm
from .models import Customer


def customer_list(request):

    customers = Customer.objects.all()

    return render(
        request,
        "customers/customer_list.html",
        {
            "customers": customers,
        },
    )


def customer_detail(
    request,
    pk,
):

    customer = get_object_or_404(
        Customer,
        pk=pk,
    )

    return render(
        request,
        "customers/customer_detail.html",
        {
            "customer": customer,
        },
    )


def customer_create(request):

    if request.method == "POST":

        form = CustomerForm(
            request.POST,
        )

        if form.is_valid():

            customer = form.save()

            messages.success(
                request,
                "Customer created successfully.",
            )

            return redirect(
                "customers:customer_detail",
                pk=customer.pk,
            )

    else:

        form = CustomerForm()

    return render(
        request,
        "customers/customer_form.html",
        {
            "form": form,
            "page_title": "Add Customer",
        },
    )


def customer_update(
    request,
    pk,
):

    customer = get_object_or_404(
        Customer,
        pk=pk,
    )

    if request.method == "POST":

        form = CustomerForm(
            request.POST,
            instance=customer,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Customer updated successfully.",
            )

            return redirect(
                "customers:customer_detail",
                pk=customer.pk,
            )

    else:

        form = CustomerForm(
            instance=customer,
        )

    return render(
        request,
        "customers/customer_form.html",
        {
            "form": form,
            "customer": customer,
            "page_title": "Edit Customer",
        },
    )


def customer_delete(
    request,
    pk,
):

    customer = get_object_or_404(
        Customer,
        pk=pk,
    )

    if request.method == "POST":

        customer.delete()

        messages.success(
            request,
            "Customer deleted successfully.",
        )

        return redirect(
            "customers:customer_list",
        )

    return render(
        request,
        "customers/customer_confirm_delete.html",
        {
            "customer": customer,
        },
    )
