from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Вы авторизовались")
            return redirect('home')

        else:
            messages.error(request, 'Вы не правильно ввели логин или пароль')
            return redirect('login')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Пользователь с таким именем уже существует')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Данная почта уже используется')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth.login(request, user)
                    messages.success(request, "Вы авторизовались")
                    return redirect('home')
                    user.save()
                    messages.success(request, "Регистрация прошла успешно")
                    return redirect('home')
        else:
            messages.error(request, 'Вы не правильно вели пороль')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    return redirect('home')