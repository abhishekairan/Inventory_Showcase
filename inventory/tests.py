from django.test import TestCase

# Create your tests here.

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

for i in categories:
    print(i)