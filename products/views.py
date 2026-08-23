from django.contrib import messages

from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from .forms import ProductForm
from .models import Product



def home(request):
    products = Product.objects.all()
    
    return render(
        request,
        "home.html",
        {
            "products": products,
        },
    )    


def product_list(request):

    products = Product.objects.all()

    return render(
        request,
        "products/product_list.html",
        {
            "products": products,
        },
    )


def product_detail(
    request,
    pk,
):

    product = get_object_or_404(
        Product,
        pk=pk,
    )

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
        },
    )


def product_create(request):

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            product = form.save()

            messages.success(
                request,
                "Product created successfully.",
            )

            return redirect(
                "products:product_detail",
                pk=product.pk,
            )

    else:

        form = ProductForm()

    return render(
        request,
        "products/product_form.html",
        {
            "form": form,
            "page_title": "Add Product",
        },
    )


def product_update(
    request,
    pk,
):

    product = get_object_or_404(
        Product,
        pk=pk,
    )

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Product updated successfully.",
            )

            return redirect(
                "products:product_detail",
                pk=product.pk,
            )

    else:

        form = ProductForm(
            instance=product,
        )

    return render(
        request,
        "products/product_form.html",
        {
            "form": form,
            "product": product,
            "page_title": "Edit Product",
        },
    )


def product_delete(
    request,
    pk,
):

    product = get_object_or_404(
        Product,
        pk=pk,
    )

    if request.method == "POST":

        product.delete()

        messages.success(
            request,
            "Product deleted successfully.",
        )

        return redirect(
            "products:product_list",
        )

    return render(
        request,
        "products/product_confirm_delete.html",
        {
            "product": product,
        },
    )
