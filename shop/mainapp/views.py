from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    product_objects = Product.objects.all()
    return render(request, 'mainapp/home.html',{'products': product_objects})

def product(request):
    return render(request, 'mainapp/product.html')

