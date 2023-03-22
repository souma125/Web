from django import forms
from main.models import *

class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model=Customer
        fields= ["first_name","last_name","age","date_of_birth","phone","email"]

class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields = "__all__"