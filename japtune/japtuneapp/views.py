from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def main(request):
    return render(request, 'japtuneapp/index.html')
