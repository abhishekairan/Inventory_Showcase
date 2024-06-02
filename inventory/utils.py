from .models import Category, ProductCategory, Product, ProductImage


def get_header_template_content():
    
    context = {}
    display_category = Category.objects.all().filter(display=True)
    
    for a in display_category:
        context[a] = [product_category for product_category in ProductCategory.objects.all().filter(main_category=a).filter(display=True)]
    
    return context # -> {<Category: Clothing>: [<ProductCategory: Men's T-Shirts>, <ProductCategory: Children's Jackets>, <ProductCategory: Women's Skirts>, <ProductCategory: Men's Suits>, <ProductCategory: Athletic Wear>, <ProductCategory: Underwear & Socks>]}

def get_new_product_section_context():
    
    context = {}
    newProducts = Product.objects.all().order_by('-created_at')[:5]
    for a in newProducts:
        try:
            images = ProductImage.objects.all().filter(product = a).filter(is_default = True)[0]
        except:
            images = ProductImage.objects.all().filter(product = a)[0]
        context[a] = images
    print(context)
    return context