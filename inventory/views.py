from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
import random
from .models import Category, Product


# Create your views here.

def generate_data(request):
    fake = Faker()

    # Define product categories
    categories = [
        "Electronics",
        "Clothing",
        "Books",
        "Home & Kitchen",
        "Toys & Games",
        "Sports & Outdoors",
        "Beauty & Personal Care",
        "Health & Household",
        "Automotive",
        "Grocery & Gourmet Food"
    ]

    def generate_random_product():
        # Generate a random product name
        product_name = fake.word().capitalize() + ' ' + fake.word().capitalize()

        # Generate a random product cost between $5 and $500
        product_cost = round(random.uniform(5, 500), 2)

        # Select a random category from the list
        product_category = random.choice(categories)

        return product_name, product_cost, product_category

    def generate_random_category_name():
        # Generate a random category name
        return fake.word().capitalize()

    def generate_random_category_description():
        # Generate a random category description
        return fake.sentence(nb_words=10)

    def generate_random_category():
        # Generate a random category name and description
        category_name = generate_random_category_name()
        category_description = generate_random_category_description()
        return category_name, category_description

    # Generate and print 10 random products
    # for index in range(10):
    #     catdescription = generate_random_category_description()
    #     Category.objects.create(name=categories[index],description=catdescription)
    #     print(f"Category Name: {categories[index]}, Description: {catdescription} has been added successfully")
    for index in range(10):
        name, cost, category = generate_random_product()
        Product.objects.create(name=name, cost=cost, category=Category.objects.get(name=random.choice(categories)),
                               description=generate_random_category_description())
        print(f"Product Name: {name}, Cost: ${cost}, Category: {category} has been added successfully")
    return HttpResponse(f"Added new products successfully")


def product(request):
    return render(request, 'product.html')

def sample_template(request):
    return render(request,'sample-templates/sample-template-loader.html')