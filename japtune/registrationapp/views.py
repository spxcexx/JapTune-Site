from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):
    if request.method == "POST":
        first_name = request.POST.get("name")
        last_name = request.POST.get("surname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        text_error = None
        print(f"Ім'я: {first_name}; Фамілія {last_name}; Email: {email}; Юзернейм: {username}; Пароль: {password}; Підтв. пароля:{password_confirm}")
        if password == password_confirm:
            try:
                print("Спроба створити юзера")
                User.objects.create_user(first_name=first_name, last_name=last_name ,email=email, username=username, password=password)
                print("Користувача створено")
                return redirect('login')
            except IntegrityError:
                print("Користувач існує")
                text_error = "Такий користувач вже існує"
                return render(request, "registrationapp/registration.html", context={"text_error" : text_error})
        elif password != password_confirm:
            text_error = "Паролі не збігаються"
            return render(request, "registrationapp/registration.html", context={"text_error" : text_error})

        else:
            text_error = "Помилка"
            return render(request, "registrationapp/registration.html", context={"text_error" : text_error})

    return render(request, 'registrationapp/registration.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        text_error = None
        print(f"Аунтифікація користувача. Юзернейм: {username}; Пароль: {password}")
        user = authenticate(request, username=username, password=password)
        print("Користувач аунтифікувався. Перевірка у базі данних")
        if user is not None:
            print("Користувача знайдено")
            login(request, user)
            return redirect("successful_login")
        else:
            print("Користувача не знайдено")
            text_error = "Такого користувача не знайдено"
            return render(request, "registrationapp/autorization.html", context={"text_error" : text_error})
    return render(request, 'registrationapp/autorization.html' )

def show_successful_login(request):
    if request.user.is_authenticated:
        return render(request, "japtuneapp/index.html")
    else:
        return redirect("login")

def logout_user(request):
    logout(request)
    return redirect("login")
