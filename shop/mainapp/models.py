# from unicodedata import category
# from certifi import contents
from django.db import models
# from numpy import product
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()

# Create your models here.

# Созд моделей
# 1 - Category
# 2 - Product
# 3 - CartProduct
# 4 - Cart
# 5 - Order

# 6 - Customer
# 7 - Specification

class Category(models.Model):
    
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):  
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    discription = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2,verbose_name='Цена')
    
    def __str__(self):
        return self.title
   

class Parameter(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    value = models.CharField(max_length=255, verbose_name="Значение")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    product = models.ForeignKey(to=Product, verbose_name="Товар", related_name="parameter", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.value}"


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    # product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    final_prace = models.DecimalField(max_digits=9, decimal_places=2,verbose_name='Общая стоимость')
    
    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)
    

class Cart(models.Model):
    
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_prace = models.DecimalField(max_digits=9, decimal_places=2,verbose_name='Общая стоимость')
    
    def __str__(self):
        return str(self.id)
    
    
class Customer(models.Model):
    
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    adress = models.CharField(max_length=255, verbose_name='Адрес')
    
    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)
