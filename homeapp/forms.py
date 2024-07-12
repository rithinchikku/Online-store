from django import forms
from .models import Book


class Bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

        widgets={

            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'enter name...!'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'enter price...!'})
        }


