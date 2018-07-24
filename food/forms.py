from django import forms
from django.forms import ModelForm, DateTimeInput


from .models import FoodItem


class AddItem(ModelForm):
    class Meta:
        model = FoodItem
        widgets = {'date_added': DateTimeInput(attrs={'class': 'datepicker'})}
        fields = ['item', 'date_added']
