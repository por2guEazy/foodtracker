from django import forms
from django.forms import ModelForm, DateTimeInput


from .models import FoodItem, UserProfile


# Add a food item 
class AddItem(ModelForm):
    class Meta:
        model = FoodItem
        widgets = {'date_added': DateTimeInput(attrs={'class': 'datepicker'})}
        fields = ['item', 'amount', 'calories', 'date_added']




# Enter user info
class EditProfile(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['height', 'weight']



# Select menu to view items by choice
class ViewItemsByDate(forms.Form):
    options = (('today', 'Today'), ('yesterday', 'Yesterday'), ('last-week', 'Last Week'))
    field = forms.ChoiceField(label='', choices=options)
