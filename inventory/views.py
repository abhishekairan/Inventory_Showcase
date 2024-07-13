from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest as Request
from .models import Category, ProductCategory
from .utils import get_header_template_content, get_newArrival_product_section_context, get_featured_product_section_context, get_product_context, get_all_product_context,get_searched_product_context


# Create your views here.


def product_content(request,id):
    header_context = get_header_template_content()
    product_context = get_product_context(int(id))
    return render(request,'product.html',context={
        "header_context" : header_context,
        "product_context": product_context
    })

def sample_template(request):
    context = get_header_template_content()
    return render(request,'sample-templates/sample-template-loader.html',context={'categories': context})


def home(request):
    header_context = get_header_template_content()
    product_section_context = get_newArrival_product_section_context(10)
    featured_product_section_context = get_featured_product_section_context(10)
    product_list_context = get_all_product_context()
    print(product_section_context)
    return render(request,'home.html',context={
        'header_context':header_context,
        'newArrival_product_section':product_section_context,
        'featured_product_section': featured_product_section_context,
        'products_list_context': product_list_context,
        'product_page_title': 'All Products',
        'title':'Home'
    })
    
    
def products(request: Request,filter_type: str=None):
    header_context = get_header_template_content()
    title=''
    product_context={}
    if filter_type=='new_arrival':
        title = 'New Arrival'
        product_context = get_newArrival_product_section_context(100)
    elif filter_type=='featured':
        title = "Featured"
        product_context = get_featured_product_section_context(100)
    elif filter_type=="all_product":
        title = "All Products"
        product_context = get_all_product_context()
    elif request.method == "GET":
        search = request.GET.get('s')
        product_context = get_searched_product_context(search)
        title = f"Results for {search}"
    
    return render(request,'products.html',context={
        'title':title,
        'product_page_title':title,
        'header_context': header_context,
        'products_list_context': product_context
    })
    
def categorys(request,id:int):
    categorysObject = Category.objects.get(category_id=id)
    category_context = get_all_product_context(category=categorysObject)
    # print(f"category_context: {category_context}")
    header_context = get_header_template_content()
    return render(request,'products.html',context={
        'title':categorysObject.name,
        'products_list_context': category_context,
        'header_context':header_context,
        'product_page_title':categorysObject.display_name
    })
    
def category(request,id:int):
    categoryObject = ProductCategory.objects.get(category_id=id)
    category_context = get_all_product_context(category=categoryObject)
    header_context = get_header_template_content()
    return render(request,'products.html',context={
        'title':categoryObject.name,
        'products_list_context': category_context,
        'header_context':header_context,
        'product_page_title':categoryObject.display_name
    })
    