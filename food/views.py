from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from .forms import AddItem, EditProfile
from .models import FoodItem, UserProfile


# Index view - required login 
@login_required(login_url='/food/login/')
def index(request):
    view = 'food/index.html'
    # Get a list of food based on specific user that is logged in
    food_list = FoodItem.objects.filter(user_id=request.user).order_by('-date_added')
    # Create form
    add_item_form = AddItem()

    if request.method == 'POST':
        add_item_form = AddItem(request.POST)
        # Validate data
        if add_item_form.is_valid():
            item =  add_item_form.save(commit=False)
            item.user = request.user
            item.save()
            
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


# Profile view w/ required login
@login_required(login_url='/food/login/')
def profile(request):
    view = 'food/profile.html'
    # Make query to get user info
    user_info = UserProfile.objects.filter(user_id=request.user).first()
    # Create form 
    form_data = EditProfile(instance=user_info)
    # Calculate & round BMI to 2 decimals 
    bmi = str(round( ((user_info.weight) / (user_info.height**2)) * 703, 2))

    if request.method == 'POST':
        # Check if that instance exists, update or save new data
        form_data = EditProfile(request.POST, instance=user_info)
        # Validate data
        if form_data.is_valid():
            item =  form_data.save(commit=False)
            item.user = request.user
            item.save()
           
            context = { 
                'bmi': bmi,
                'user_data_form': form_data, 
                'user_info': user_info,
            }

    else:
        context = { 
                'bmi': bmi,
                'user_data_form': form_data,
                'user_info': user_info,
        } 

    return render(request, view, context)
