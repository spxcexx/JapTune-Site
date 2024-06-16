from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ім'я")
    email = forms.EmailField(label='Ел. пошта')
    message = forms.CharField(widget=forms.Textarea, label='Ваш текст')
