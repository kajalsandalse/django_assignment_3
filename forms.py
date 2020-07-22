from django import forms
class MyForm(forms.Form):
    username=forms.CharField(label="Username",max_length=100)
    password=forms.CharField(label="password",widget=forms.PasswordInput)
    phone=forms.CharField(label="Phone No.",max_length=100)
    address=forms.CharField(label="Address",max_length=100)