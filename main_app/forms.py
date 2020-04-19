from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=250)
    email_address = forms.CharField(label='E-Mail-Address', max_length=250)
