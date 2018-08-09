from django.contrib import admin

# Register your models here.
from .models import FoodItem, UserProfile

admin.site.register(FoodItem)

admin.site.register(UserProfile)
