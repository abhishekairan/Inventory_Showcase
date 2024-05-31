from .models import Category, ProductCategory


def get_header_template_content():
    display_category = Category.objects.all().filter(display=True)
    for a in display_category:
        print(a.name)