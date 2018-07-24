from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from .models import FoodItem, AddItem

# Index view - required login 
@login_required(login_url='/food/login/')
def index(request):

    view = 'food/index.html'
    ai = AddItem()
    # Get a list of food based on specific user that is logged in
    food_list = FoodItem.objects.filter(user_id=request.user).order_by('-date_added')
    context = {
            'latest_food_items': food_list,
            'add_form': ai, 
    }

    return render(request, view, context)



