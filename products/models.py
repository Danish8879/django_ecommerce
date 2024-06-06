from django.db import models
from base.models import BaseModel
from django.utils.text import slugify # a method which generates slug automatically 


# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True ,null= True, blank=True)
    category_image = models.ImageField(upload_to="categories")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name) # Generate a slug from the category_name and assign it to the slug field
        super(Category,self).save(*args, **kwargs) # Call the original save method from the parent class to handle the actual saving process

    def __str__(self) -> str:
        return self.category_name    

class Product(BaseModel):
    product_name= models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null= True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name) # Generate a slug from the product_name and assign it to the slug field
        super(Product,self).save(*args, **kwargs) # Call the original save method from the parent class to handle the actual saving process

    def __str__(self) -> str:
        return self.product_name   


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="product_images")
    image = models.ImageField(upload_to="product")

    

class ColorVariant(BaseModel):
    color_name= models.CharField(max_length=100)
    price =models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.color_name   

class SizeVariant(BaseModel):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.size_name   

