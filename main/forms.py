from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    text = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'rows': '1'})
    )

    class Meta:
        model = Order
        fields = ('name', 'phone', 'email', 'text', 'theme')

