from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest as Request
from django.contrib.auth.models import User
from django.contrib.auth import login as userlogin, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inventory.utils import *

# Create your views here.


def login(request: Request):
        try:
            if request.user.is_authenticated:
                return redirect('/dashboard/')
            if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                user_obj = User.objects.filter(username=username)
                if not user_obj.exists():
                    messages.info(request,"Invalid username")
                    return redirect('/login/')
                user_obj = authenticate(request,username=username,password= password)
                if user_obj and user_obj.is_superuser:
                    userlogin(request, user_obj)
                    messages.info(request,"Logged in")
                    return redirect('/dashboard/')
                messages.info(request,'Invalid Password')
                return redirect('/login/')
            
            return render(request,'dashboard/login.html')
        except Exception as e:
                    print(e)
                    
                    
                    
@login_required(login_url='login')
def dashboard(request):
    product_count = get_all_product_context().count()
    context = {
        'product_count': product_count,
    }
    return render(request, 'dashboard/dashboard.html',context=context)


@login_required(login_url='login')
def product(request: Request):
    product = get_all_product_context()
    featured_product = product.filter(featured=True)
    discounts = get_discount()
    context = {
        'product_count': len(product),
        'featured_product_count': len(featured_product),
        'products': product,
        'discounts': discounts
    }
    return render(request,'dashboard/product.html',context=context)