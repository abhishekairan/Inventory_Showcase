import os
from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    display = models.BooleanField(blank=False,default=True)
    
    def __str__(self):
        return self.name
    
class ProductCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    display = models.BooleanField(blank=False,default=True)
    main_category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name="parent_category")
    
    def __str__(self):
        return self.display_name

    

class Discount(models.Model):
    value = models.IntegerField()
    discountType = models.CharField("Discount Type",'discountType',choices=[('%','%'),('₹','₹')],max_length=2,default='%')

    def __str__(self):
        if self.discountType == '%':
            return f'{self.value}{self.discountType}'
        else:
            return f'{self.discountType}{self.value}'
            
    


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    description = models.TextField()
    additional_details = models.TextField(blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False,blank=False)

    def __str__(self):
        return self.name
    
    @property
    def get_discount_price(self):
        if self.discount:
            if self.discount.discountType == '%':
                return self.cost - (self.cost * (self.discount.value/100))
            else:
                return self.cost - self.discount.value
        else:
            return self.cost
    
    @property
    def default_image(self):
        default_image = ProductImage.objects.filter(product = self, is_default = True)
        if default_image.exists():
            return default_image[0]
        else:
            try:
                default_image = ProductImage.objects.filter(product = self)[0]
            except:
                default_image = ProductImage.objects.filter(product = self)
        return default_image
                
    @property
    def thumbnail_image(self):
        thumbnail_image = ProductImage.objects.filter(product = self, is_default = True)
        if thumbnail_image.exists():
            return thumbnail_image[0]
        else:
            return None

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE,blank=True,null=True)
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=100, blank=True, null=True)

    is_default = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_default:
            ProductImage.objects.filter(product=self.product, is_default=True).update(is_default=False)
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        image_path = self.image.path
        self.image.delete()
        if os.path.exists(image_path):
            os.remove(image_path)
        super(ProductImage, self).delete(*args, **kwargs)
        
        
    def __str__(self):
        return f"Image for {self.id}"
