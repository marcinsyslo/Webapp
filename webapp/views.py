from django.shortcuts import render
from .models import Product, User


def home(request):
    return render(request, 'home.html')


def users(request):
    all_users = User.objects.all()
    context = {
        'all_users': all_users
    }
    return render(request, 'users.html', context)


def user(request):
    current_user = request.user
    context = {
        'user': current_user
    }
    return render(request, 'user.html', context)


def products(request):
    all_products = Product.objects.all()
    context = {
        'products': all_products
    }
    return render(request, 'products.html', context)


def product(request, product_id):
    this_product = Product.objects.get(pk=product_id)
    context = {
        'product': this_product
    }
    return render(request, 'product.html', context)
