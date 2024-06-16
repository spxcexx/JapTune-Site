from django.shortcuts import render

# Create your views here.

def subaru_view(request):
    return render(request, 'subaru/index.html')
