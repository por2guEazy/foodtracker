from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import AddItem
from .models import FoodItem


# Index view - required login 
@login_required(login_url='/food/login/')
def index(request):

    view = 'food/index.html'
    # Get a list of food based on specific user that is logged in
    food_list = FoodItem.objects.filter(user_id=request.user).order_by('-date_added')
    

    if request.method == 'POST':
        add_item_form = AddItem(request.POST)
        print("STUFF: " + str(request.POST))
        if add_item_form.is_valid():
            view = 'food/added.html'
            print("AYYYYOOO")

    else:
        add_item_form = AddItem()
    
    
    context = {
            'latest_food_items': food_list,
            'add_form': add_item_form, 
    }            


    return render(request, view, context)





