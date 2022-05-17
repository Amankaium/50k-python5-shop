from django.contrib import admin
from .models import *


'''
from django import forms
class NotebookCategoryChoiceField(forms.ModelChoiceField):
    
    pass
    
    
class NotebookAdmin(admin.ModelAdmin):
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return NotebookCategoryChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    
class SmatrphoneCategoryChoiceField(forms.ModelChoiceField):
    
    pass
    
    
class SmartphoneAdmin(admin.ModelAdmin):
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return NotebookCategoryChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
'''
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
