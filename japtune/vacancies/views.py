from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
def vacancies_view(request):
    return render(request, 'vacancies/index.html')

def administrator_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        middlename = request.POST.get('middlename', '')
        age = request.POST.get('age', '')
        desc = request.POST.get('desc', '')
        email = request.POST.get('email', '')


        try:
            send_mail(
                subject='Заявка на вакансію адміністратора',
                message=f"""
                Ім'я: {name}
                Прізвище: {surname}
                По-батькові: {middlename}
                Вік: {age}
                Ел. пошта: {email}
                Контактна інформація та трохи про себе:
                {desc}
                """,
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'vacancies/index.html')
        except Exception as e:
            return render(request, 'vacancies/index.html')

    return render(request, 'vacancies/administrator.html')


def cleaner_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        middlename = request.POST.get('middlename', '')
        age = request.POST.get('age', '')
        desc = request.POST.get('desc', '')
        email = request.POST.get('email', '')


        try:
            send_mail(
                subject='Заявка на вакансію прибиральника',
                message=f"""
                Ім'я: {name}
                Прізвище: {surname}
                По-батькові: {middlename}
                Вік: {age}
                Ел. пошта: {email}
                Контактна інформація та трохи про себе:
                {desc}
                """,
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'vacancies/index.html')
        except Exception as e:
            return render(request, 'vacancies/index.html')

    return render(request, 'vacancies/cleaner.html')

def mechanic_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        middlename = request.POST.get('middlename', '')
        age = request.POST.get('age', '')
        desc = request.POST.get('desc', '')
        email = request.POST.get('email', '')


        try:
            send_mail(
                subject='Заявка на вакансію механіка',
                message=f"""
                Ім'я: {name}
                Прізвище: {surname}
                По-батькові: {middlename}
                Вік: {age}
                Ел. пошта: {email}
                Контактна інформація та трохи про себе:
                {desc}
                """,
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'vacancies/index.html')
        except Exception as e:
            return render(request, 'vacancies/index.html')

    return render(request, 'vacancies/mechanic.html')

def mechanics_helper_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        middlename = request.POST.get('middlename', '')
        age = request.POST.get('age', '')
        desc = request.POST.get('desc', '')
        email = request.POST.get('email', '')


        try:
            send_mail(
                subject='Заявка на вакансію помічника автомеханіка',
                message=f"""
                Ім'я: {name}
                Прізвище: {surname}
                По-батькові: {middlename}
                Вік: {age}
                Ел. пошта: {email}
                Контактна інформація та трохи про себе:
                {desc}
                """,
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'vacancies/index.html')
        except Exception as e:
            return render(request, 'vacancies/index.html')

    return render(request, 'vacancies/mechanics_helper.html')

def supply_manager_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        middlename = request.POST.get('middlename', '')
        age = request.POST.get('age', '')
        desc = request.POST.get('desc', '')
        email = request.POST.get('email', '')


        try:
            send_mail(
                subject='Заявка на вакансію менеджера з постачання',
                message=f"""
                Ім'я: {name}
                Прізвище: {surname}
                По-батькові: {middlename}
                Вік: {age}
                Ел. пошта: {email}
                Контактна інформація та трохи про себе:
                {desc}
                """,
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'vacancies/index.html')
        except Exception as e:
            return render(request, 'vacancies/index.html')

    return render(request, 'vacancies/supply_manager.html')

def tire_mechanic_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        middlename = request.POST.get('middlename', '')
        age = request.POST.get('age', '')
        desc = request.POST.get('desc', '')
        email = request.POST.get('email', '')


        try:
            send_mail(
                subject='Заявка на вакансію шиномонтажника',
                message=f"""
                Ім'я: {name}
                Прізвище: {surname}
                По-батькові: {middlename}
                Вік: {age}
                Ел. пошта: {email}
                Контактна інформація та трохи про себе:
                {desc}
                """,
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'vacancies/index.html')
        except Exception as e:
            return render(request, 'vacancies/index.html')

    return render(request, 'vacancies/tire_mechanic.html')
