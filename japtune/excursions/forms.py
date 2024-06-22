from django import forms

class ExcursionsForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ім'я", widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    email = forms.EmailField(label='Ел. пошта', widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    phone = forms.CharField(label='Ваш номер телефону', widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
