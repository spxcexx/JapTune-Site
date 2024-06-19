from django.shortcuts import render
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
        # name = request.POST.get("name")
        # email = request.POST.get("email")
        form = OrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']


            send_mail(
                subject=f'Нове повідомлення від {name}',
                message=f'Ел. пошта відправника: {email}',
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect('/success/')
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return render(request, 'honda/detailsNSX.html')



# def order_view(request):

