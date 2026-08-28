from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    dob = forms.DateField()
    email = forms.EmailField()