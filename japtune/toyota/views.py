from django.shortcuts import render

# Create your views here.

def toyota_view(request):
    return render(request, 'toyota/toyota.html')

def detailsSupra_view(request):
    return render(request, 'toyota/detailsSupra.html')

def detailsTrueno_view(request):
    return render(request, 'toyota/DetailsTrueno.html')
