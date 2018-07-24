from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from .forms import AddItem
from .models import FoodItem


# Index view - required login 
@login_required(login_url='/food/login/')
def index(request):

    view = 'food/index.html'
    # Get a list of food based on specific user that is logged in
    food_list = FoodItem.objects.filter(user_id=request.user).order_by('-date_added')
    
    add_item_form = AddItem()

    if request.method == 'POST':
        add_item_form = AddItem(request.POST)

        if add_item_form.is_valid():
            item =  add_item_form.save(commit=False)
            item.user = request.user
            item.save()

           # view = 'food/added.html'
           # food_item = add_item_form.cleaned_data['item']
           # date = add_item_form.cleaned_data['date_added']
           # user_inputs = [food_item, date]

            context = {
                'latest_food_items': food_list,
                'add_form': add_item_form, 
            }

    else:
    
        context = {
            'latest_food_items': food_list,
            'add_form': add_item_form, 
        }            


    return render(request, view, context)





