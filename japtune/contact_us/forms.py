from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ім'я", widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    email = forms.EmailField(label='Ел. пошта', widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    message = forms.CharField(label='Ваш текст', widget=forms.Textarea(attrs={'class': 'form-control mb-3', 'style': 'width: 300px; height: 150px; resize: none;'}))
