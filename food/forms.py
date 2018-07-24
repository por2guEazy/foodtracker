from django import forms
from models import FoodItem




class AddItem(ModelForm):
    class Meta:
        model = FoodItem
        widgets = {'date': DateInput(attrs={'class': 'datepicker'})}

        fields = ['item', 'date_added']
