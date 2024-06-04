from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
import random
from .models import Category, Product, ProductCategory, Discount
from .utils import get_header_template_content, get_newArrival_product_section_context, get_featured_product_section_context, get_product_context, get_all_product_context


# Create your views here.

def generate_data(request):
    fake = Faker()

    # Define product categories
    categories = {
    "Electronics": [
        "Smartphones",
        "Laptops",
        "Tablets",
        "Headphones",
        "Smartwatches",
        "Digital Cameras",
        "Bluetooth Speakers",
        "Gaming Consoles",
        "Televisions",
        "Portable Chargers"
    ],
    "Clothing": [
        "Men's T-Shirts",
        "Women's Dresses",
        "Children's Jackets",
        "Men's Jeans",
        "Women's Skirts",
        "Baby Onesies",
        "Women's Blouses",
        "Men's Suits",
        "Athletic Wear",
        "Underwear & Socks"
    ],
    "Books": [
        "Fiction Novels",
        "Non-Fiction Books",
        "Children's Books",
        "Self-Help Books",
        "Cookbooks",
        "Science Fiction",
        "Biographies",
        "Historical Novels",
        "Fantasy Books",
        "Mystery & Thriller Books"
    ],
    "Home & Kitchen": [
        "Cookware Sets",
        "Blenders",
        "Coffee Makers",
        "Dishware Sets",
        "Bedding Sets",
        "Vacuum Cleaners",
        "Air Purifiers",
        "Cutlery Sets",
        "Food Storage Containers",
        "Toasters"
    ],
    "Toys & Games": [
        "Action Figures",
        "Board Games",
        "Plush Toys",
        "Puzzles",
        "Lego Sets",
        "Remote Control Cars",
        "Dollhouses",
        "Educational Toys",
        "Outdoor Playsets",
        "Building Blocks"
    ],
    "Sports & Outdoors": [
        "Exercise Equipment",
        "Camping Tents",
        "Hiking Boots",
        "Bicycles",
        "Yoga Mats",
        "Fishing Gear",
        "Sports Apparel",
        "Water Bottles",
        "Tennis Rackets",
        "Golf Clubs"
    ],
    "Beauty & Personal Care": [
        "Skincare Products",
        "Haircare Products",
        "Makeup Kits",
        "Perfumes",
        "Nail Polish",
        "Shaving Kits",
        "Sunscreens",
        "Bath Bombs",
        "Hair Dryers",
        "Electric Toothbrushes"
    ],
    "Health & Household": [
        "Vitamins & Supplements",
        "First Aid Kits",
        "Cleaning Supplies",
        "Air Fresheners",
        "Blood Pressure Monitors",
        "Thermometers",
        "Laundry Detergent",
        "Health Monitors",
        "Humidifiers",
        "Disinfectant Wipes"
    ],
    "Automotive": [
        "Car Accessories",
        "Car Care Kits",
        "Tire Pressure Gauges",
        "Car Covers",
        "Jump Starters",
        "GPS Systems",
        "Car Seat Covers",
        "Dashboard Cameras",
        "Motor Oil",
        "Windshield Wipers"
    ],
    "Grocery & Gourmet Food": [
        "Snacks",
        "Beverages",
        "Organic Foods",
        "Condiments",
        "Spices",
        "Pasta & Rice",
        "Breakfast Cereals",
        "Canned Foods",
        "Baking Supplies",
        "Gourmet Chocolates"
    ]
}

    def generate_random_product(category):
        # choicing a random product name from categories 
        product_name = random.choice(categories[category])

        # Generate a random product cost between $5 and $500
        product_cost = round(random.uniform(5, 500), 2)

        return product_name, product_cost

    def generate_random_category_name():
        # Generate a random category name
        return random.choice()
    
    def generate_random_sub_category_name(category):
        # Generate a random category name
        return random.choice(category)

    def generate_random_category_description():
        # Generate a random category description
        return fake.sentence(nb_words=10)

    def generate_random_category():
        # Generate a random category name and description
        category_name = generate_random_category_name()
        category_description = generate_random_category_description()
        return category_name, category_description
    
    def generate_random_boolean():
        return random.choice([True,False])

    for cate in categories:
        description = generate_random_category_description()
        display = generate_random_boolean()
        cat_obj = Category.objects.create(name=cate,display_name=cate,description=description,display=display)
        for subcat in categories[cate]:
            description = generate_random_category_description()
            display = generate_random_boolean()
            ProductCategory.objects.create(name=subcat,display_name=subcat,description=description,display=display,main_category=cat_obj)
    
    for discount in range(0,101,5):
        Discount.objects.create(value=discount,discountType = '%')
    for discount in range(100,1001,100):
        Discount.objects.create(value=discount,discountType = '₹')
    return HttpResponse(f"Added new products successfully")


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
    return render(request,'home.html',context={
        'header_context':header_context,
        'newArrival_product_section':product_section_context,
        'featured_product_section': featured_product_section_context,
        'products_list_context': product_list_context,
        'product_page_title': 'All Products',
        'title':'Home'
    })
    
    
def products(request,filter_type: str=None):
    header_context = get_header_template_content()
    if filter_type=='new_arrival':
        title = 'New Arrival'
        product_context = get_newArrival_product_section_context(100)
    elif filter_type=='featured':
        title = "Featured"
        product_context = get_featured_product_section_context(100)
    elif filter_type=="all_product":
        title = "All Products"
        product_context = get_all_product_context()
    return render(request,'products.html',context={
        'title':title,
        'product_page_title':title,
        'header_context': header_context,
        'products_list_context': product_context
    })