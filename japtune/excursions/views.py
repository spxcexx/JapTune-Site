from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ExcursionsForm
# Create your views here.

def excursions_view(request):
    if request.method == 'POST':
        form = ExcursionsForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            
            send_mail(
                subject=f'Новий запис на екскурсію',
                message=f"{name}\n Номер телефону: {phone}\n Ел. пошта: {email}",
                from_email=email,
                recipient_list=['dimasnovikov330@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'japtuneapp/index.html', {'form': form})

    else:
        form = ExcursionsForm()
    return render(request, 'excursions/index.html', {'form': form})


