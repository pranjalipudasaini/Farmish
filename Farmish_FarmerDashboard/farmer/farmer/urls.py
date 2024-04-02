"""
URL configuration for farmer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main.views import frontpage, about, contactus, Myshop, Orders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('about/', about, name='about'),
    path('contactus/', contactus, name='contactus'),
    path('Myshop/', Myshop, name='Myshop'),
    path('', include('userprofile.urls')),
    path('Orders/', Orders, name='Orders'),
    path('', include('MyShop.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

