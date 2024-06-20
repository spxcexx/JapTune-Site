from django.shortcuts import render

# Create your views here.

def nissan_view(request):
    return render(request, 'nissan/nissan.html')

def detailsSkyline_view(request):
    # if request.method == 'POST':
    #     print(11111111)
    #     # name = request.POST.get("name")
    #     # email = request.POST.get("email")
    #     form = OrderForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']


    #         send_mail(
    #             subject=f'Нове повідомлення від {name}',
    #             message=f'Ел. пошта відправника: {email}',
    #             from_email=email,
    #             recipient_list=['dimasnovikov330@gmail.com'],
    #             fail_silently=False,
    #         )
    #         return HttpResponseRedirect('/success/')
    #     else:
    #         return JsonResponse({'success': False, 'errors': form.errors})
    return render(request, 'nissan/detailsSkyline.html')



# def order_view(request):

def detailsSilvia_view(request):
    # if request.method == 'POST':
    #     print(11111111)
    #     # name = request.POST.get("name")
    #     # email = request.POST.get("email")
    #     form = OrderForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']


    #         send_mail(
    #             subject=f'Нове повідомлення від {name}',
    #             message=f'Ел. пошта відправника: {email}',
    #             from_email=email,
    #             recipient_list=['dimasnovikov330@gmail.com'],
    #             fail_silently=False,
    #         )
    #         return HttpResponseRedirect('/success/')
    #     else:
    #         return JsonResponse({'success': False, 'errors': form.errors})
    return render(request, 'nissan/detailsSilvia.html')
