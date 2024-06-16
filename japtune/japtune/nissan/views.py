from django.shortcuts import render

# Create your views here.

def nissan_view(request):
    return render(request, 'nissan/index.html')
