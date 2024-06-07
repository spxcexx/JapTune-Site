from django.shortcuts import render

# Create your views here.

def honda_view(request):
    return render(request, 'honda/honda.html')
