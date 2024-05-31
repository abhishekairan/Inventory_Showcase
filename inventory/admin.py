from django.contrib import admin
from inventory.models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id','name','display_name','description','display')
    search_fields = ('name','catergory_id')

@admin.register(ProductCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id','name','display_name','description','main_category','display')
    search_fields = ('name','catergory_id','parent')
    

@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name','percentage')
    search_fields = ('name',)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'product_id', 'category', 'discount', 'created_at', 'updated_at')
    search_fields = ('product_id','name')
    list_filter = ('category','tags','discount')
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'alt_text')
    search_fields = ('product__name',)

