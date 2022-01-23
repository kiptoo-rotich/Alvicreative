from dataclasses import field
from django import forms
from django.core.validators import RegexValidator
from .models import RequestService

def My_TextField_Validator(self):
    return RegexValidator(r'^[-a-zA-Z0-9. ]+$',
    'Valid Input: Alphanumeric characters, dash, dot, space')

class RequestForm(forms.ModelForm):
    Full_name = forms.CharField(max_length=50, min_length=4, required=True,
                           help_text='', label='',
                           validators=[My_TextField_Validator],
                           widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Enter your full name'}))

    Phone_number = forms.CharField(required=True,
                           help_text='', label='',
                           validators=[My_TextField_Validator],
                           widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Phone number'}))  

    Email_address = forms.CharField(max_length=50, min_length=4, required=True,
                           help_text='', label='',
                           validators=[My_TextField_Validator],
                           widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'johndoe@gmail.com'}))  

    Message = forms.CharField(required=True,
                           help_text='', label='',
                           validators=[My_TextField_Validator],
                           widget=forms.Textarea(attrs={'class': 'form-control', 
                           'placeholder': 'My message is ...'}))    
     
    class Meta:
        model:RequestService
        fields='__all__'