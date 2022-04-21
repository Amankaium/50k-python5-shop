from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        print('POST method fdfdsasfdsa')
        return redirect('home')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        messages.error(request, "this is error request")
        return redirect('register')
    else:
        return render(request, ('accounts/register.html'))
    #     firstname = request.POST['firstname']
    #     lastname = request.POST['lastname']
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     confirm_password = request.POST['confirm_password']
    #     if password == confirm_password:
    #         if User.objects.filter(username=username).exists():
    #             messages.error(request, 'username already exist')
    #             return redirect('register')
    #         else:
    #             if User.objects.filter(email=email).exists():
    #                 messages.error(request, 'email already exist')
    #                 return redirect('register')
    #             else:
    #                 user = User.objects.create_user(first_name=firstname, last_name=lastname, user_name=username, email=email, password=password)
    #                 auth.login(request, user)
    #                 messages.success(request, "You are logged in")
    #                 return redirect('home')
    #                 user.save()
    #                 messages.success(request, "You are registered successfully")
    #                 return redirect('login')
    #     else:
    #         messages.error(request, 'password do not match')
    #         return redirect('register')
    # else:
    #     return render(request, 'accounts/register.html')

def logout(request):
    return redirect('home')