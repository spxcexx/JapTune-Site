

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from honda.forms import OrderForm
# Create your views here.

def toyota_view(request):
    return render(request, 'toyota/toyota.html')

def detailsSupra_view(request):
    if request.method == 'POST':
        print(11111111)
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        with_tune = request.POST.get("tuning")
        without_tune = request.POST.get("without_tuning")

        form = OrderForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            with_tune = request.POST.get("tuning")



            send_mail(
                subject=f'Нове замовлення (Toyota Supra)',
                message=f"Ел. пошта відправника: {email}\n Ім'я: {name} \n Номер телефону: {phone} \n Тюнінг: {with_tune}",
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'toyota/toyota.html')
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return render(request, 'toyota/detailsSupra.html')

def detailsTrueno_view(request):
    if request.method == 'POST':
        print(11111111)
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        with_tune = request.POST.get("tuning")
        without_tune = request.POST.get("without_tuning")

        form = OrderForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            with_tune = request.POST.get("tuning")



            send_mail(
                subject=f'Нове замовлення (Toyota Trueno)',
                message=f"Ел. пошта відправника: {email}\n Ім'я: {name} \n Номер телефону: {phone} \n Тюнінг: {with_tune}",
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'toyota/toyota.html')
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return render(request, 'toyota/DetailsTrueno.html')
