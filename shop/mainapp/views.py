from django.shortcuts import render,get_object_or_404
from cart_shop.forms import CartAddProductForm
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def home(request):
    products = Product.objects.all()

    data = {
        'products': products,
    }
    return render(request, 'mainapp/home.html', data)




def product(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'mainapp/product.html', {'products': product,
                                                        'cart_product_form': cart_product_form})    



def base(request):
    products = Product.objects.all()

    data = {
        'products': products,
    }
    return render(request, 'mainapp/base.html', data)