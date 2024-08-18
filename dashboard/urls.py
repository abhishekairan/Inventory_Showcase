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
    path('dashboard/category/<str:id>',category,name='Dcategory'),
    path('dashboard/new-category',newCategory,name='Newcategory'),
    path('dashboard/delete-category/<str:id>',deleteCategory,name='DeleteCategory'),
    path('dashboard/add-category',addCategory,name='add-category'),
    
    path('dashboard/tags',tags,name='dashboard-tags'),
    path('dashboard/tag/<str:id>',tag,name='Dtag'),
    path('dashboard/new-tag',newTag,name='Newtag'),
    path('dashboard/delete-tag/<str:id>',deleteTag,name='DeleteTag'),
    path('dashboard/add-tag',addTag,name='add-tag'),
    
    
    path('dashboard/discounts',discounts,name='dashboard-discount'),
    path('dashboard/discount/<str:id>',discount,name='Ddiscount'),
    path('dashboard/new-discount',newDiscount,name='Newdiscount'),
    path('dashboard/delete-discount/<str:id>',deleteDiscount,name='DeleteDiscount'),
    path('dashboard/add-discount',addDiscount,name='add-discount'),
    
    path('dashboard/user',users,name='dashboard-users'),
    
    path('search/product/',search_product,name='search-product'),
    path('search/category/',search_category,name='search-category'),
    path('search/tags/',search_tags,name='search-tags'),
    path('search/discounts/',search_discounts,name='search-discounts'),
    path('search/users/',search_users,name='search-users'),
    path('add-product-image/', add_product_image, name='add-product-image'),
]
