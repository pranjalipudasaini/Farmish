from django.shortcuts import render

def frontpage(request):
    return render(request, 'main/Farmerdashboard.html')

def about(request):
    return render(request, 'main/about.html')

def contactus(request):
    return render(request, 'main/contactus.html')

def Myshop(request):
    return render(request, 'main/Myshop.html')

def Orders(request):
    return render(request, 'main/Orders.html')
