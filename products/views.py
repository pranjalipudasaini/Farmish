# products/views.py
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib import messages

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully added!')
            return redirect('product_list')  # Redirect to product list page
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/shop.html', {'products': products})