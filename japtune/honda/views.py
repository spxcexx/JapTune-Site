from django.shortcuts import render
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import OrderForm

# Create your views here.

def honda_view(request):
    return render(request, 'honda/index.html')

def detailsNSX_view(request):
    return render(request, 'honda/detailsNSX.html')



def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']


            send_mail(
                'Новый заказ (Honda NSX)',
                f'Имя: {name}\nЭл. почта: {email}',
                'dimasnovikov330@gmail.com',
                [email],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
