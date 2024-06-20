from .models import Category, ProductCategory, Product, ProductImage, Discount
from typing import Union
from django.db.models import Q
from django.contrib.auth.models import User
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def get_header_template_content():
    
    context = {}
    display_category = Category.objects.all().filter(display=True)
    
    for a in display_category:
        context[a] = [product_category for product_category in ProductCategory.objects.all().filter(main_category=a).filter(display=True)]
    
    return context # -> {<Category: Clothing>: [<ProductCategory: Men's T-Shirts>, <ProductCategory: Children's Jackets>, <ProductCategory: Women's Skirts>, <ProductCategory: Men's Suits>, <ProductCategory: Athletic Wear>, <ProductCategory: Underwear & Socks>]}




def get_product_images(product: Product):
    images = ProductImage.objects.all().filter(product= product).order_by('-is_default')
    return images

def get_image(id:int):
    image = ProductImage.objects.get(id=id)
    return image

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
    # print(category)
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
    # print(context)
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
    if featured in ['True','False']:
        product_context = product_context.filter(featured=featured)
        # print('Products got filtered by featured')
    return product_context

def get_products(id:int=None):
    if id != None:
        products = Product.objects.filter(product_id = id)
    else:
        products = Product.objects.all()
    return products

def get_discount(value:str=None):
    if value != None:
        newvalue = value.replace('%'," %").replace('₹',"₹ ").split()
        if(newvalue[0]=='₹'):
            discounttype = newvalue[0]
            discountamount = int(newvalue[1])
        else:
            discounttype = newvalue[1]
            discountamount = int(newvalue[0])
        discount = Discount.objects.get(value= discountamount, discountType=discounttype)
    else:
        discount = Discount.objects.all()
    return discount

def get_categories():
    categories = Category.objects.all()
    return categories

def get_tags(id:int=None):
    if id != None:
        tags = ProductCategory.objects.get(category_id=id)
    else:
        tags = ProductCategory.objects.all()
    return tags

def get_users():
    users = User.objects.all()
    return users

def get_product_categories():
    tags = ProductCategory.objects.all()
    return tags


def get_searched_category_context(search_query,display=None):
    categories = Category.objects.all()
    if search_query!=None:
        categories = categories.filter(Q(name__icontains=search_query) | Q(description__icontains = search_query))
    if display in ['True','False']:
        categories = categories.filter(display=display)
        # print('Products got filtered by featured')
    return categories

def get_searched_tags_context(search_query,display=None):
    tags = ProductCategory.objects.all()
    # print(display)
    if search_query!=None:
        tags = tags.filter(Q(name__icontains=search_query) | Q(description__icontains = search_query))
    if display in ['True','False']:
        tags = tags.filter(display=display)
        # print('Products got filtered by featured')
    return tags

def get_searched_users_context(search_query,display=None):
    users = User.objects.all()
    # print(display)
    if search_query!=None:
        users = users.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains = search_query) | Q(username__icontains = search_query) | Q(email__icontains = search_query))
    if display in ['True','False']:
        users = users.filter(is_superuser=display)
        # print('Products got filtered by featured')
    return users

def save_image(image_url):
    response = requests.get(image_url)
    print(response)
    if response.status_code == 200:
        print("If condition fullfilled")
        file_name = image_url.split("/")[-1]
        print(f"file_name: {file_name}")
        file_content = ContentFile(response.content)
        print(f"file_content: {file_content}")
        file_path = default_storage.save(f'images/{file_name}', file_content)

def add_or_update_product(queryset):
    images = {}
    kwargs = {}
    product_id = None
    for key, value in queryset:
        # print(f"{key}: {value}")
        if key == 'csrfmiddlewaretoken':
            pass
        elif key == 'product-id':
            product_id = value
        elif key=='product_name_input':
            kwargs['name'] = value
        elif key == 'product_cost_input':
            kwargs['cost'] = value
        elif key == 'product_discount_input':
            kwargs['discount'] = get_discount(value)
        elif key == 'product_tag_input':
            kwargs['category'] = get_tags(value)
        elif key == 'featured':
            kwargs['featured'] = value
        elif key == 'product_description_input':
            kwargs['description'] = value
        elif key == 'product_additional_details_input':
            kwargs['additional_details'] = value
        else:
            images[key] = value
            
    # print(images)
    for key, value in images.items():
        if key=='default_image':
            if str.isnumeric(value):
                image = get_image(value)
                image.is_default = True
                image.save()
            else:
                # print(value)
                save_image(value)
                
    if product_id != None:
        product = get_products(product_id)
        product.update(**kwargs)
    else:
        product = Product.objects.create(**kwargs)