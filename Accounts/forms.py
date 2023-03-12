from django import forms
from .models import Account



class RegisterationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your firstname',
        'class':'form-control'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your lastname',
        'class':'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email address & must be valid one',
        'class':'form-control'
    }))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder':'Your phonenumber',
        'class':'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'form-control'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm your password',
        'class':'form-control'
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

    def __init__(self, *args, **kwargs):
        super(RegisterationForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(RegisterationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Your password confirmation doesnot match')






























































































