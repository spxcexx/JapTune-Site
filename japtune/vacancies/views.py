from django.shortcuts import render

# Create your views here.
def vacancies_view(request):
    return render(request, 'vacancies/index.html')
