from django import forms
from .models import Signup


class SignupForm(forms.ModelForm):

    class Meta:
        model = Signup
        fields = ['first_name','last_name','username','password', 'confirm_password', 'role','email','address','pincode', 'state','city','pic']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form', 'placeholder': 'Firstname'}),
             
             'last_name':forms.TextInput(attrs={'class': 'form', 'placeholder': 'Lastname'}),
             'username':forms.TextInput(attrs={'class': 'form', 'placeholder': 'Username'}),
             'password':forms.TextInput(attrs={'class': 'form', 'placeholder': 'Password'}),
             'confirm_password':forms.TextInput(attrs={'class': 'form', 'placeholder': 'Confirm_password'}),
             'role':forms.Select(attrs={'class': 'form'}),

             'email':forms.EmailInput(attrs={'class': 'form', 'placeholder': 'Email'}),
             'address':forms.TextInput(attrs={'class': 'form', 'placeholder': 'Address'}),
             'pincode': forms.NumberInput(attrs={'class': 'form', 'placeholder': '411011'}),
             'state':forms.TextInput(attrs={'class': 'form', 'placeholder': 'Maharashtra'}),
             'city':forms.TextInput(attrs={'class': 'form', 'placeholder': 'Mumbai'}),
             'pic': forms.FileInput(attrs={'class': 'form'}),

        }
        def clean(self):
            cleaned_data = super(SignupForm, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
               raise forms.ValidationError(
                  "password and confirm_password does not match"
                )
            return cleaned_data

        #fields = "__all__"
        #fields = ['name', 'hotel_Main_Img']
