from .models import Category, ProductCategory, Product, ProductImage


def get_header_template_content():
    
    context = {}
    display_category = Category.objects.all().filter(display=True)
    
    for a in display_category:
        context[a] = [product_category for product_category in ProductCategory.objects.all().filter(main_category=a).filter(display=True)]
    
    return context # -> {<Category: Clothing>: [<ProductCategory: Men's T-Shirts>, <ProductCategory: Children's Jackets>, <ProductCategory: Women's Skirts>, <ProductCategory: Men's Suits>, <ProductCategory: Athletic Wear>, <ProductCategory: Underwear & Socks>]}



def get_product_default_image(product: Product):
    try:
        images = ProductImage.objects.all().filter(product = product).filter(is_default = True)[0]
    except:
        try:
            images = ProductImage.objects.all().filter(product = product)[0]
        except:
            images = None
    return images


def get_product_images(product: Product):
    images = ProductImage.objects.all().filter(product= product).order_by('-is_default')
    return images


def get_newArrival_product_section_context(limit:int=0):
    context = {}
    if limit == 0:
        newProducts = Product.objects.all().order_by('-created_at')
    else:
        newProducts = Product.objects.all().order_by('-created_at')[:limit]
    for a in newProducts:
        context[a] = get_product_default_image(a)
    print(context)
    return context



def get_featured_product_section_context(limit: int = 0):
    context = {}
    if limit == 0:
        featuredProducts = Product.objects.all().order_by('-featured')
    else:
        featuredProducts = Product.objects.all().order_by('-featured')[:limit]
    for product in featuredProducts:
        context[product] = get_product_default_image(product)
    return context

        


def get_all_product_context(limit:int = 0):
    context = {}
    if limit != 0:
        allproducts = Product.objects.all()[:limit]
    else:
        allproducts = Product.objects.all()
    for product in allproducts:
        context[product] = get_product_default_image(product)
    return context
        


def get_product_context(id:int):
    context = {}
    product = Product.objects.filter(product_id = id)[0]
    context[product] = get_product_images(product)
    print(context)
    return context