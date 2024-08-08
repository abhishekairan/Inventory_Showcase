from .models import Category, ProductCategory, Product, ProductImage, Discount
from typing import Union
from django.db.models import Q
from django.contrib.auth.models import User

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
    image = ProductImage.objects.filter(id=id)
    if image.exists():
        return image[0]
    else:
        return None

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

def get_categories(id:int = None):
    if id:
        categories = Category.objects.all().filter(category_id=id)
    else: 
        categories = Category.objects.all()
    return categories

def get_tags(id:int=None):
    if id != None:
        tags = ProductCategory.objects.all().filter(category_id=id)
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

def add_or_update_product(queryset):
    images = {}
    kwargs = {}
    product_id = None
    kwargs['featured'] = False
    for key, value in queryset:
        # print(f"{key}: {value}")
        match key:
            case 'csrfmiddlewaretoken':
                pass
            case 'product-id':
                product_id = value
            case 'product_name_input':
                kwargs['name'] = value
            case 'product_cost_input':
                kwargs['cost'] = value
            case 'product_discount_input':
                kwargs['discount'] = get_discount(value)
            case 'product_tag_input':
                kwargs['category'] = get_tags(value)[0]
            case 'featured':
                kwargs['featured'] = True
            case 'product_description_input':
                kwargs['description'] = value
            case 'product_additional_details_input':
                kwargs['additional_details'] = value
            case _:
                images[key] = value
    # print(kwargs)
    if product_id != None:
        product = get_products(product_id)
        product.update(**kwargs)
        product=product[0]
    else:
        product = Product.objects.create(**kwargs)
        
    exsistingImages = list(get_product_images(product))
    exsistingImage = [image.id for image in exsistingImages ]
    for key, value in images.items():
        if key=='default_image':
            image = get_image(value)
            if(image):
                image.is_default = True
                image.save()
        else:
            image = get_image(key)
            image.product = product
            image.save()
            try:
                exsistingImage.remove(image.id)
            except:
                pass
    for imageID in exsistingImage:
        image = get_image(imageID)
        image.delete()
    return product

def clearCache():
    productImages = ProductImage.objects.all().filter(product=None)
    for image in productImages:
        image.delete()
        
def add_or_update_category(queryset):
    category_id = None
    kwargs = {}
    kwargs['display'] = False
    for key, value in queryset:
        # print(key,value)
        match(key):
            case 'csrfmiddlewaretoken':
                pass
            case 'category-id':
                category_id = value
            case 'category_name_input':
                kwargs['name'] = value
            case 'category_displayName_input':
                kwargs['display_name'] = value
            case 'category_description_input':
                kwargs['description'] = value
            case 'display':
                kwargs['display'] = True
    if category_id != None:
        category = get_categories(category_id)
        category.update(**kwargs)
    else:
        category = Category.objects.create(**kwargs)
    return category
        
def add_or_update_tag(queryset):
    tag_id = None
    kwargs = {}
    kwargs['display'] = False
    for key,value in queryset:
        match key:
            case 'csrfmiddlewaretoken':
                pass
            case 'tag-id':
                tag_id = value
            case 'tag_name_input':
                kwargs['name'] = value
            case 'tag_displayName_input':
                kwargs['display_name'] = value
            case 'tag_description_input':
                kwargs['description'] = value
            case 'tag_category':
                kwargs['main_category'] = get_categories(int(value))[0]
            case 'display':
                kwargs['display'] = True
    if tag_id != None:
        tag = get_tags(tag_id)
        tag.update(**kwargs)
    else:
        tag = ProductCategory.objects.create(**kwargs)
    return tag