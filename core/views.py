from django.shortcuts import render
from products.models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    
    return render(
        request,
        "home.html",
        {
            "products": products,
        },
    )    


def dashboard(request):
    products = Product.objects.all()
    
    return render(
        request,
        "products/product_list.html",
        {
            "products": products,
        },
    )