from django.shortcuts import render

# Create your views here.
def our_works_view(request):
    return render(request, 'our_works/index.html')
