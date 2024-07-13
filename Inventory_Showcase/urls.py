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
from django.conf.urls.static import static
from django.conf import settings
from inventory.views import product_content, sample_template,home,products,category,categorys

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/<int:id>',product_content),
    path('sample-template',sample_template),
    path('products/<str:filter_type>',products),
    path('products/',products,name='products'),
    path('category/<int:id>',category),
    path('categorys/<int:id>',categorys),
    path('',home),
    path('home',home,name='home'),
    path('',include('dashboard.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)