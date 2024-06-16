from django.shortcuts import render

# Create your views here.
def our_address_view(request):
    return render(request, 'our_address/index.html')
