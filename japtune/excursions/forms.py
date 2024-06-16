from django import forms

class ExcursionsForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ім'я")
    email = forms.EmailField(label='Ел. пошта')
    phone = forms.CharField(widget=forms.Textarea, label='Ваш номер телефону')
