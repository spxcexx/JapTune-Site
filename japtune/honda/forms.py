from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(label="Ім'я", max_length=100)
    email = forms.EmailField(label='Ел. пошта')
    