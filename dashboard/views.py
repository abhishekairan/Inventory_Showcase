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
    category_count = get_categories().count()
    tags_count = get_tags().count()
    user_count = get_users().count()
    discount_count = get_discount().count()
    context = {
        'product_count': product_count,
        'category_count': category_count,
        'tags_count': tags_count,
        'user_count': user_count,
        'discount_count': discount_count,
    }
    clearCache()
    return render(request, 'dashboard/dashboard.html',context=context)


@login_required(login_url='login')
def products(request: Request):
    product = get_all_product_context()
    featured_product = product.filter(featured=True)
    discounts = get_discount()
    context = {
        'product_count': len(product),
        'featured_product_count': len(featured_product),
        'products': product,
        'discounts': discounts
    }
    return render(request,'dashboard/product/products.html',context=context)

@login_required(login_url='login')
def product(request: Request,id):
    product = get_product_context(id)
    discounts = get_discount()
    tags = get_tags()
    context = {
        'products': product,
        'discounts': discounts,
        'tags': tags
    }
    # print(product)
    return render(request,'dashboard/product/product.html',context=context)

@login_required(login_url='login')
def newProduct(request: Request):
    discounts = get_discount()
    tags = get_tags()
    context = {
        'discounts': discounts,
        'tags': tags
    }
    # print(product)
    return render(request,'dashboard/product/newproduct.html',context=context)


@login_required(login_url='login')
def deleteProduct(request: Request,id):
    product = get_products(int(id))
    product.delete()
    # print(product)
    return redirect('dashboard-product')


@login_required(login_url='login')
def addProduct(request: Request):
    if request.method == "POST":
        add_or_update_product(request.POST.items())
    return redirect('dashboard-product')

@login_required(login_url='login')
def categories(request: Request):
    categories = get_categories()
    context = {
        'category_count': len(categories),
        'display_category': len(categories.filter(display= True)),
        'categories': categories,
    }
    return render(request,'dashboard/category/categories.html',context=context)


@login_required(login_url='login')
def category(request: Request,id):
    category = get_categories(id)[0]
    context = {
        'category': category,
    }
    return render(request,'dashboard/category/category.html',context=context)

@login_required(login_url='login')
def newCategory(request: Request):
    return render(request,'dashboard/category/newcategory.html')


@login_required(login_url='login')
def deleteCategory(request: Request,id):
    product = get_categories(int(id))
    product.delete()
    # print(product)
    return redirect('dashboard-category')


@login_required(login_url='login')
def addCategory(request: Request):
    if request.method == "POST":
        print(request.POST)
        add_or_update_category(request.POST.items())
    return redirect('dashboard-category')


# Discount Functions

@login_required(login_url='login')
def discounts(request: Request):
    discounts = get_discount()
    context = {
        'discount_count': len(discounts),
        # 'display_tags': len(tags.filter(display= True)),
        'discounts': discounts,
    }
    return render(request,'dashboard/discount/discounts.html',context=context)


@login_required(login_url='login')
def discount(request: Request,id):
    discounts = get_discount(id=id)[0]
    context = {
        'discount': discounts,
    }
    return render(request,'dashboard/discount/discount.html',context=context)

@login_required(login_url='login')
def newDiscount(request: Request):
    return render(request,'dashboard/discount/newDiscount.html')


@login_required(login_url='login')
def deleteDiscount(request: Request,id):
    discount = get_discount(id=id)
    discount.delete()
    # print(product)
    return redirect('dashboard-discount')


@login_required(login_url='login')
def addDiscount(request: Request):
    if request.method == "POST":
        print(request.POST)
        add_or_update_discount(request.POST.items())
    return redirect('dashboard-discount')


# Tags Functions

@login_required(login_url='login')
def tags(request: Request):
    tags = get_tags()
    context = {
        'tags_count': len(tags),
        'display_tags': len(tags.filter(display= True)),
        'tags': tags,
    }
    return render(request,'dashboard/tags/tags.html',context=context)


@login_required(login_url='login')
def tag(request: Request,id):
    tags = get_tags(id)[0]
    categories = get_categories()
    context = {
        'tag': tags,
        'categories':categories
    }
    return render(request,'dashboard/tags/tag.html',context=context)

@login_required(login_url='login')
def newTag(request: Request):
    categories = get_categories()
    context = {
        'categories':categories
    }
    return render(request,'dashboard/tags/newtag.html',context=context)


@login_required(login_url='login')
def deleteTag(request: Request,id):
    product = get_tags(int(id))
    product.delete()
    # print(product)
    return redirect('dashboard-tags')


@login_required(login_url='login')
def addTag(request: Request):
    if request.method == "POST":
        print(request.POST)
        add_or_update_tag(request.POST.items())
    return redirect('dashboard-tags')


# User functions

@login_required(login_url='login')
def users(request: Request):
    users = get_users()
    context = {
        'users_count': len(users),
        'super_users': len(users.filter(is_superuser= True)),
        'users': users,
    }
    return render(request,'dashboard/user/users.html',context=context)


# Search Functions

def search_product(request: Request):
    if request.method == "POST":
        search_query = request.POST.get('inputval')
        featured = request.POST.get('featuredval')
        # print(search_query)
        # print(featured)
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
    
    
def search_tags(request: Request):
    if request.method == "POST":
        search_query = request.POST.get('inputval')
        display = request.POST.get('featuredval')
        # print(search_query)
        # print(display)
        category = get_searched_tags_context(search_query,display)
        response_data={
            'message':'success',
            'input_value': serialize('json',category)
        }
        return JsonResponse(response_data,safe=False)


def search_discounts(request: Request):
    if request.method == "POST":
        search_query = request.POST.get('inputval')
        display = request.POST.get('featuredval')
        # print(search_query)
        # print(display)
        discount = get_searched_discounts_context(search_query,display)
        response_data={
            'message':'success',
            'input_value': serialize('json',discount)
        }
        return JsonResponse(response_data,safe=False)
    
    
def search_users(request: Request):
    if request.method == "POST":
        search_query = request.POST.get('inputval')
        display = request.POST.get('featuredval')
        # print(search_query)
        # print(display)
        users = get_searched_users_context(search_query,display)
        response_data={
            'message':'success',
            'input_value': serialize('json',users)
        }
        return JsonResponse(response_data,safe=False)
    
    
    
def add_product_image(request: Request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        product_image = ProductImage.objects.create(image=image)
        context = {
            'success': True,
            'image_id': product_image.id,
            'image_url': product_image.image.url
        }
        return JsonResponse(context)
    return JsonResponse({'success': False})