from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')

def product(request):
    return render(request, 'mainapp/product.html')
