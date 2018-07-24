from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, DateTimeInput
from django.contrib.admin.widgets import AdminDateWidget


class UserProfile(models.Model):
    # Don't need to add unique=True because one-one does that
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)


# Model for food eaten item to add to list
# Add more fields later to better classify
class FoodItem(models.Model):
    item = models.CharField(max_length=50)
    date_added = models.DateTimeField('Date added')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item



class AddItem(ModelForm):
    class Meta:
        model = FoodItem
        widgets = {'date_added': DateTimeInput(attrs={'class': 'datepicker'})}
        fields = ['item', 'date_added']