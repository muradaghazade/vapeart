from django import forms 
from .models import Order

class CreateOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['full_name', 'number', 'email', 'address', 'price']

        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'first_name', 'placeholder': 'Ad Soyad Ata adı',  'class': 'form-control yes_req memory-field'}),
            'number': forms.TextInput(attrs={'id': 'phone', 'placeholder': 'Məsələn, +994 (10) 555-4567',  'class': 'form-control yes_req memory-field vapeghost__phone'}),
            'email': forms.TextInput(attrs={'id': 'number', 'placeholder': 'Məsələn, example@example.ru',  'class': 'form-control yes_req memory-field'}),
            'address': forms.Textarea(attrs={'id': 'deliveri', 'placeholder': 'Tam unvani daxil edin',  'class': 'form-control memory-field'}),
            'price': forms.NumberInput(attrs={'id': 'price-form', 'placeholder': '123-456-7890', 'class': 'd-none'}),
        }