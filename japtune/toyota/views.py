from django.shortcuts import render

# Create your views here.

def toyota_view(request):
    return render(request, 'toyota/toyota.html')
