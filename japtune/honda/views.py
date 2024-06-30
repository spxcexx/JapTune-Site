
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .forms import OrderForm

# Create your views here.

def honda_view(request):
    return render(request, 'honda/index.html')

def detailsNSX_view(request):
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
                subject=f'Нове замовлення (Honda NSX)',
                message=f"Ел. пошта відправника: {email}\n Ім'я: {name} \n Номер телефону: {phone} \n Тюнінг: {with_tune}",
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'honda/index.html')
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return render(request, 'honda/detailsNSX.html')


def detailsIntegra_view(request):
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
                subject=f'Нове замовлення (Honda Integra)',
                message=f"Ел. пошта відправника: {email}\n Ім'я: {name} \n Номер телефону: {phone} \n Тюнінг: {with_tune}",
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'honda/index.html')
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return render(request, 'honda/detailsIntegra.html')
