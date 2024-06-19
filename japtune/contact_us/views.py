from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
# Create your views here.

def contact_us_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f'Нове повідомлення від {name}',
                message=f'Ел. пошта відправника: {email} \n Текст повідомлення: {message}',
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,

            )
            return HttpResponseRedirect('/success/')
    else:
        form = ContactForm()
    return render(request, 'contact_us/index.html', {'form': form})

def success_view(request):
    return render(request, 'contact_us/success.html')

