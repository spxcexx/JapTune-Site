from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from honda.forms import OrderForm
# Create your views here.

def mazda_view(request):
    return render(request, 'mazda/mazda.html')

def rx_7_view(request):
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
                subject=f'Нове замовлення (Mazda RX-7)',
                message=f"Ел. пошта відправника: {email}\n Ім'я: {name} \n Номер телефону: {phone} \n Тюнінг: {with_tune}",
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'mazda/rx-7.html')
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return render(request, 'mazda/rx-7.html')


def mx_5_view(request):
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
                subject=f'Нове замовлення (Mazda MX-5)',
                message=f"Ел. пошта відправника: {email}\n Ім'я: {name} \n Номер телефону: {phone} \n Тюнінг: {with_tune}",
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'mazda/mx-5.html')
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return render(request, 'mazda/mx-5.html')
