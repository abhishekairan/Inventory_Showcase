"""
URL configuration for Inventory_Showcase project.

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
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/',login,name="login"),
    path('dashboard/',dashboard, name="dashboard"),
    path('dashboard/product',products,name='dashboard-product'),
    path('dashboard/product/<str:id>',product,name='Dproduct'),
    path('dashboard/new-product',newProduct,name='Newproduct'),
    path('dashboard/delete-product/<str:id>',deleteProduct,name='DeleteProduct'),
    path('dashboard/add-product',addProduct,name='add-product'),
    path('dashboard/category',categories,name='dashboard-category'),
    path('dashboard/tags',tags,name='dashboard-tags'),
    path('dashboard/user',users,name='dashboard-users'),
    path('search/product/',search_product,name='search-product'),
    path('search/category/',search_category,name='search-category'),
    path('search/tags/',search_tags,name='search-tags'),
    path('search/users/',search_users,name='search-users'),
    path('add-product-image/', add_product_image, name='add-product-image'),
]
