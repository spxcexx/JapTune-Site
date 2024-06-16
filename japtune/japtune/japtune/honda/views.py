from django.shortcuts import render


# Create your views here.

def honda_view(request):
    return render(request, 'honda/index.html')

def details_view(request):
    return render(request, 'honda/details.html')
