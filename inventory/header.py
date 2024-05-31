from .models import Category, ProductCategory


def get_header_template_content():
    
    context = {}
    display_category = Category.objects.all().filter(display=True)
    
    for a in display_category:
        context[a] = [product_category for product_category in ProductCategory.objects.all().filter(main_category=a).filter(display=True)]
    
    return context # -> {<Category: Clothing>: [<ProductCategory: Men's T-Shirts>, <ProductCategory: Children's Jackets>, <ProductCategory: Women's Skirts>, <ProductCategory: Men's Suits>, <ProductCategory: Athletic Wear>, <ProductCategory: Underwear & Socks>], <Category: Home & Kitchen>: [<ProductCategory: Cookware Sets>, <ProductCategory: Blenders>, <ProductCategory: Coffee Makers>, <ProductCategory: Dishware Sets>, <ProductCategory: Toasters>], <Category: Toys & Games>: [<ProductCategory: Board Games>, <ProductCategory: Puzzles>, <ProductCategory: Remote Control Cars>, <ProductCategory: Educational Toys>, <ProductCategory: Outdoor Playsets>, <ProductCategory: Building Blocks>], <Category: Beauty & Personal Care>: [<ProductCategory: Skincare Products>, <ProductCategory: Nail Polish>, <ProductCategory: Shaving Kits>, <ProductCategory: Bath Bombs>, <ProductCategory: Hair Dryers>, <ProductCategory: Electric Toothbrushes>], <Category: Health & Household>: [<ProductCategory: Cleaning Supplies>, <ProductCategory: Blood Pressure Monitors>, <ProductCategory: Thermometers>], <Category: Automotive>: [<ProductCategory: Car Care Kits>, <ProductCategory: Tire Pressure Gauges>, <ProductCategory: Car Covers>, <ProductCategory: Car Seat Covers>, <ProductCategory: Dashboard Cameras>, <ProductCategory: Windshield Wipers>], <Category: Grocery & Gourmet Food>: [<ProductCategory: Snacks>, <ProductCategory: Beverages>, <ProductCategory: Organic Foods>, <ProductCategory: Canned Foods>]}