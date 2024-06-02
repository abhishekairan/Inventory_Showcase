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
        return str(self.value)
    


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

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=100, blank=True, null=True)

    is_default = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_default:
            ProductImage.objects.filter(product=self.product, is_default=True).update(is_default=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.product.name}"
