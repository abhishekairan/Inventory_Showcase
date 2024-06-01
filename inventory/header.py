from .models import Category, ProductCategory


def get_header_template_content():
    
    context = {}
    display_category = Category.objects.all().filter(display=True)
    
    for a in display_category:
        context[a] = [product_category for product_category in ProductCategory.objects.all().filter(main_category=a).filter(display=True)]
    
    return context # -> {<Category: Clothing>: [<ProductCategory: Men's T-Shirts>, <ProductCategory: Children's Jackets>, <ProductCategory: Women's Skirts>, <ProductCategory: Men's Suits>, <ProductCategory: Athletic Wear>, <ProductCategory: Underwear & Socks>]}