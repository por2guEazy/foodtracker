from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

import datetime
from datetime import timedelta
from django.utils import timezone


from .forms import AddItem, EditProfile, ViewItemsByDate 
from .models import FoodItem, UserProfile


""" 
    Function Based Views
"""

# Index view - required login 
@login_required(login_url='/food/login/')
def index(request):
        
    # Create forms for page
    add_item_form = AddItem()
    view_items_by_date = ViewItemsByDate()

    # Update db with new food item
    item_post(request)



    # View food by date given
    food_list = view_by_date(request)

    context = {
        'latest_food_items': food_list,
        'add_form': add_item_form,
        'view_by_date_form': view_items_by_date, 
    }

    return render(request, 'food/index.html', context)


# Profile view w/ required login
@login_required(login_url='/food/login/')
def profile(request):
    view = 'food/profile.html'
    # Make query to get user info
    user_info = UserProfile.objects.filter(user_id=request.user).first()
    # Create form 
    form_data = EditProfile()
    
    # Handle profile edit post request
    profile_post(request, user_info)
      
    context = { 
            'bmi': get_bmi(user_info.height, user_info.weight),
            'user_data_form': form_data,
            'user_info': user_info,
    } 

    return render(request, view, context)



"""
    Helper functions
"""

# Calculate BMI
def get_bmi(height, weight):
    if height == 0:
        bmi = 'N/A'
    else:
        bmi = str(round( ((weight) / (height**2)) * 703, 2))

    return bmi



# Handle item post request
def item_post(request):
    # Handle add items by date form
    if request.method == 'POST':
        add_item_form = AddItem(request.POST)
        # Validate data
        if add_item_form.is_valid():
            item =  add_item_form.save(commit=False)
            item.user = request.user
            item.save()
            
            return redirect('index') 



# Handle profile edit post request
def profile_post(request, user_info):
    if request.method == 'POST':
        # Check if that instance exists, update or save new data
        form_data = EditProfile(request.POST, request.FILES, instance=user_info)
        # Validate data
        if form_data.is_valid():
            item =  form_data.save(commit=False)
            item.user = request.user
            item.save()
           
            return redirect('profile')



# Allow user to remove any given item from list
def remove_item(request, pk):
    # Get the item by PK
    item = get_object_or_404(FoodItem, pk=pk)
    # Delete specific item
    if request.method == 'POST':
        item.delete()
        
        return redirect('index')




# Display food items by given date
def view_by_date(request):
   
    # Today is default
    food_list = FoodItem.objects.filter(
            user_id=request.user, 
            date_added__gte=datetime.datetime.today().replace(hour=0, minute=0).astimezone() - timedelta(0),
            date_added__lte=datetime.datetime.today().replace(hour=0, minute=0).astimezone() - timedelta(-1),
    ).order_by('-date_added')    

    # Get user input
    show_by = request.GET.get('field')

    # Handle view items by date form
    if show_by == 'yesterday':
        food_list = FoodItem.objects.filter(
            user_id=request.user, 
            date_added__gte=datetime.datetime.today().replace(hour=0, minute=0).astimezone() - timedelta(1),
            date_added__lte=datetime.datetime.today().replace(hour=0, minute=0).astimezone() - timedelta(0)
        ).order_by('-date_added')    
   
    # Items eaten in the last week
    if show_by =='last-week':
        food_list = FoodItem.objects.filter(
            user_id=request.user, 
            date_added__gte=datetime.datetime.today().replace(hour=0, minute=0).astimezone() - timedelta(7),
            date_added__lte=datetime.datetime.today().replace(hour=0, minute=0).astimezone() - timedelta(0)
        ).order_by('-date_added')

    return food_list 

