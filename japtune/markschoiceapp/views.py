from django.shortcuts import render

# Create your views here.
def main_choice(request):
    return render(request, 'markschoiceapp/markschoiceapp.html')
