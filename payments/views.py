from django.contrib import messages

from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from .forms import PaymentForm
from .models import Payment


def payment_list(request):

    payments = Payment.objects.select_related(
        "order",
        "order__customer",
    )

    return render(
        request,
        "payments/payment_list.html",
        {
            "payments": payments,
        },
    )


def payment_detail(
    request,
    pk,
):

    payment = get_object_or_404(
        Payment,
        pk=pk,
    )

    return render(
        request,
        "payments/payment_detail.html",
        {
            "payment": payment,
        },
    )


def payment_create(request):

    if request.method == "POST":

        form = PaymentForm(
            request.POST,
        )

        if form.is_valid():

            payment = form.save()

            messages.success(
                request,
                "Payment created successfully.",
            )

            return redirect(
                "payments:payment_detail",
                pk=payment.pk,
            )

    else:

        form = PaymentForm()

    return render(
        request,
        "payments/payment_form.html",
        {
            "form": form,
            "page_title": "Create Payment",
        },
    )


def payment_update(
    request,
    pk,
):

    payment = get_object_or_404(
        Payment,
        pk=pk,
    )

    if request.method == "POST":

        form = PaymentForm(
            request.POST,
            instance=payment,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Payment updated successfully.",
            )

            return redirect(
                "payments:payment_detail",
                pk=payment.pk,
            )

    else:

        form = PaymentForm(
            instance=payment,
        )

    return render(
        request,
        "payments/payment_form.html",
        {
            "form": form,
            "payment": payment,
            "page_title": "Edit Payment",
        },
    )


def payment_delete(
    request,
    pk,
):

    payment = get_object_or_404(
        Payment,
        pk=pk,
    )

    if request.method == "POST":

        payment.delete()

        messages.success(
            request,
            "Payment deleted successfully.",
        )

        return redirect(
            "payments:payment_list",
        )

    return render(
        request,
        "payments/payment_confirm_delete.html",
        {
            "payment": payment,
        },
    )
