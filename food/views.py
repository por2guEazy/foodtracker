from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import datetime
from datetime import timedelta
from django.utils import timezone

from .forms import AddItem, EditProfile, ViewItemsByDate
from .models import FoodItem, UserProfile


# Index view - required login 
@login_required(login_url='/food/login/')
def index(request):
        
    # Handle add items by date form
    if request.method == 'POST':
        add_item_form = AddItem(request.POST)
        # Validate data
        if add_item_form.is_valid():
            item =  add_item_form.save(commit=False)
            item.user = request.user
            item.save()
            
            return redirect('index') 

    # Get a list of food based on specific user that is logged in
    # Display items eaten today 
    food_list = FoodItem.objects.filter(
            user_id=request.user, 
            date_added__gte=datetime.datetime.today().replace(hour=0, minute=0).astimezone()
    )    
    # Create forms for page
    add_item_form = AddItem()
    view_items_by_date = ViewItemsByDate()

    # Get input
    show_by = request.GET.get('field')
    # Handle view items by date form
    if show_by == 'yesterday':
        food_list = ['Cheese', 'Fake cheese', 'Item']             
    context = {
        'latest_food_items': food_list,
        'add_form': add_item_form,
        'view_by_date_form': view_items_by_date, 
    }
    return render(request, 'food/index.html', context)





# Calculate BMI
def get_bmi(height, weight):
    if height == 0:
        bmi = 'N/A'
    else:
        bmi = str(round( ((weight) / (height**2)) * 703, 2))

    return bmi



# Profile view w/ required login
@login_required(login_url='/food/login/')
def profile(request):
    view = 'food/profile.html'
    # Make query to get user info
    user_info = UserProfile.objects.filter(user_id=request.user).first()
    # Create form 
    form_data = EditProfile()
    # Calculate & round BMI to 2 decimals 


    if request.method == 'POST':
        # Check if that instance exists, update or save new data
        form_data = EditProfile(request.POST, instance=user_info)
        # Validate data
        if form_data.is_valid():
            item =  form_data.save(commit=False)
            item.user = request.user
            item.save()
             
            context = { 
                'bmi': get_bmi(user_info.height, user_info.weight),
                'user_data_form': form_data, 
                'user_info': user_info,
            }
            
            return render(request, view, context)

  
    context = { 
            'bmi': get_bmi(user_info.height, user_info.weight),
            'user_data_form': form_data,
            'user_info': user_info,
    } 

    return render(request, view, context)
