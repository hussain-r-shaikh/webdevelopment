from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product


def home(request):
    products = Product.objects.all()
    categories = [category[0] for category in Product.CATEGORY_CHOICES]
    print("categories - ", categories)

    category_products = []

    for category in categories:
        category_products.append({
            "category": category,
            "products": products.filter(category=category),
        })


    return render(request, "home.html", {
        "category": category,
        "products": products,
        "category_products": category_products,
    })



def product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
    )
    return render(request, "products/product_detail.html", {"product":product})


@login_required
def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        "products/product_list.html",
        {
            "products": products,
        },
    )


@login_required
def product_create(request):
    if not request.user.is_superuser:
            return redirect("/admin/")

    if request.method == "POST":

        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect("product_list")

    else:
        form = ProductForm()

    return render(
        request,
        "products/product_form.html",
        {
            "form": form,
        },
    )

@login_required
def product_update(request, pk):

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

            return redirect("product_list")

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
        },
    )

@login_required
def product_delete(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
    )

    if request.method == "POST":

        product.delete()

        return redirect("product_list")

    return render(
        request,
        "products/product_confirm_delete.html",
        {
            "product": product,
        },
    )
