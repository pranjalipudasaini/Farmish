from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

from authentication.views import index
# from authentication.views import  index, product_list_view, dashboard_consumer_view

app_name = "authentication"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup',views.signup, name="signup"),
    path('signin',views.signin, name="signin"),
    path('signout',views.signout, name="signout"),
    path('activate/<uidb64>/<token>',views.activate, name="activate"),
    # path('products/',views.product_list_view, name = "product-list"),
    # path('category/', views.category_list_view, name = "category-list"),
    path('dashboard/', views.dashboard_consumer_view, name = "consumer-dashboard" ),
    path('admin-dashboard/', views.dashboard_admin_view, name = "admin-dashboard" )
]
if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, documents_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, documents_root = settings.MEDIA_ROOT)
