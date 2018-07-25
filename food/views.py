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
    #print(food_list)
    
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


# Profile view w/ required login
@login_required(login_url='/food/login/')
def profile(request):
    view = 'food/profile.html'
    user_info = UserProfile.objects.filter(user_id=request.user).first()
    form_data = EditProfile()
    # Round BMI to two decimal places
    bmi = str(round( ((user_info.weight) / (user_info.height**2)) * 703, 2))

    if request.method == 'POST':
        form_data = EditProfile(request.POST, instance=user_info)
        if form_data.is_valid():
            # Clean user data
            item =  form_data.save(commit=False)
            item.user = request.user
            item.save()
            #height = form_data.cleaned_data['height']
            #if height == 0:
            #    height = 1
            #weight = form_data.cleaned_data['weight']


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
