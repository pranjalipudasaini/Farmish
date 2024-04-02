from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q 

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(status=Product.ACTIVE).filter(Q(title__icontains=query) | Q(description__icontains=query))
   
    return render(request, 'MyShop/search.html', {
        'query': query,
        'products': products,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'MyShop/product_detail.html', {'product': product})

