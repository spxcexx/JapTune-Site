from django.shortcuts import render

# Create your views here.

def mazda_view(request):
    return render(request, 'mazda/index.html')

