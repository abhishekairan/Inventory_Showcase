from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest as Request
from django.contrib.auth.models import User
from django.contrib.auth import login as userlogin, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inventory.utils import *
from django.http import JsonResponse
from django.db.models import Q
from django.core.serializers import serialize

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


@login_required(login_url='login')
def category(request: Request):
    categories = get_categories()
    context = {
        'category_count': len(categories),
        'display_category': len(categories.filter(display= True)),
        'categories': categories,
    }
    return render(request,'dashboard/category.html',context=context)



def search_product(request: Request):
    if request.method == "POST":
        search_query = request.POST.get('inputval')
        featured = request.POST.get('featuredval')
        print(search_query)
        print(featured)
        products = get_searched_product_context(search_query,featured)
        response_data={
            'message':'success',
            'input_value': serialize('json',products)
        }
        return JsonResponse(response_data,safe=False)
    
    
def search_category(request: Request):
    if request.method == "POST":
        search_query = request.POST.get('inputval')
        display = request.POST.get('displayval')
        # print(search_query)
        # print(display)
        category = get_searched_category_context(search_query,display)
        response_data={
            'message':'success',
            'input_value': serialize('json',category)
        }
        return JsonResponse(response_data,safe=False)