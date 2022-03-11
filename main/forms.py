from django import forms
from main.models import Order


class OrderForm(forms.ModelForm):
    comment = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'rows': '2'})
    )

    class Meta:
        model = Order
        fields = '__all__'

