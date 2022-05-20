from django.shortcuts import render,get_object_or_404
from mainapp.models import Product
from cart_shop.forms import CartAddProductForm

# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')



def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})    

