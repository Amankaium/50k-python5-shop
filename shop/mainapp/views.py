from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')

def register(request):
    return render(request, 'mainapp/register.html')

def login(request):
    return render(request, 'mainapp/login.html')
