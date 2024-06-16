from .models import Category, ProductCategory, Product, ProductImage, Discount
from typing import Union
from django.db.models import Q


def get_header_template_content():
    
    context = {}
    display_category = Category.objects.all().filter(display=True)
    
    for a in display_category:
        context[a] = [product_category for product_category in ProductCategory.objects.all().filter(main_category=a).filter(display=True)]
    
    return context # -> {<Category: Clothing>: [<ProductCategory: Men's T-Shirts>, <ProductCategory: Children's Jackets>, <ProductCategory: Women's Skirts>, <ProductCategory: Men's Suits>, <ProductCategory: Athletic Wear>, <ProductCategory: Underwear & Socks>]}




def get_product_images(product: Product):
    images = ProductImage.objects.all().filter(product= product).order_by('-is_default')
    return images


def get_newArrival_product_section_context(limit:int=0):
    if limit == 0:
        newProducts = Product.objects.all().order_by('-created_at')
    else:
        newProducts = Product.objects.all().order_by('-created_at')[:limit]
    return newProducts



def get_featured_product_section_context(limit: int = 0):
    if limit == 0:
        featuredProducts = Product.objects.all().order_by('-featured')
    else:
        featuredProducts = Product.objects.all().order_by('-featured')[:limit]
    return featuredProducts

        


def get_all_product_context(limit:int = 0,category: Union[ProductCategory,Category,None]=None):
    print(category)
    if category != None:
        if type(category) == ProductCategory:
            allproducts = Product.objects.filter(category=category)
        else:
            allproducts = Product.objects.filter(category__main_category=category)
    else:
        allproducts = Product.objects.all()
    
    if limit != 0:
        allproducts = allproducts[:limit]
    return allproducts
        


def get_product_context(id:int):
    context = {}
    product = Product.objects.filter(product_id = id)[0]
    context[product] = get_product_images(product)
    print(context)
    return context


def get_category_products_context(category: Union[Category,ProductCategory]):
    context = {}
    product_context = get_all_product_context(category=category)
    context[category] = product_context
    return context


def get_searched_product_context(search_query,featured=None):
    product_context = Product.objects.all()
    if search_query!=None:
        product_context = product_context.filter(Q(name__icontains=search_query) | Q(description__icontains = search_query))
    if featured!=None:
        product_context = product_context.filter(featured=featured)
    return product_context

def get_discount():
    discount = Discount.objects.all()
    return discount