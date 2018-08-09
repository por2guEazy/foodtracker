from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    image = models.ImageField(upload_to='static/food/media/')

    def __str__(self):
        return '%s' % (self.user)


# Model for food eaten item to add to list
# Add more fields later to better classify
class FoodItem(models.Model):
    amount = models.PositiveIntegerField(default=0)
    calories = models.PositiveIntegerField(default=0)
    item = models.CharField(max_length=50)
    date_added = models.DateTimeField('Date Added')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


