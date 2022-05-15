from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
# admin.site.register(Notebook)
# admin.site.register(Smartphone)

class ParameterAdminInline(admin.StackedInline):
    model = Parameter
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["title", "discription"]
    inlines = [ParameterAdminInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
