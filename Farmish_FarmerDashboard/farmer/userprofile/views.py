from django.contrib import messages
from django.shortcuts import render, redirect
from MyShop.forms import ProductForm
from MyShop.models import Product

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            if request.user.is_authenticated:  
                product.user = request.user
            product.save()
            messages.success(request, 'Product successfully added!')
            return redirect('myshop')  

    else:
        form = ProductForm()
    
    return render(request, 'main/Farmerdashboard.html', {'form': form})

def my_shop(request):
    products = Product.objects.filter(status='active')  
    return render(request, 'main/Myshop.html', {'products': products})

