from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()


    def __str__(self):
        return '%s %s' % (self.height, self.weight)

# Model for food eaten item to add to list
# Add more fields later to better classify
class FoodItem(models.Model):
    item = models.CharField(max_length=50)
    date_added = models.DateTimeField('Date added')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


