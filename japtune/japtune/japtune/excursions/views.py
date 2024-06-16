from django.shortcuts import render

# Create your views here.

def excursions_view(request):
    return render(request, 'excursions/index.html')
