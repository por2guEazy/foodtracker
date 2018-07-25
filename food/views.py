from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from .forms import AddItem, EditProfile
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



def profile(request):
    view = 'food/profile.html'
    user_data = EditProfile()
    bmi = 0
    if request.method == 'POST':
        user_data = EditProfile(request.POST)
        if user_data.is_valid():
            height = user_data.cleaned_data['height']
            weight = user_data.cleaned_data['weight']
            print(f"USER DATA: Height {height} Weight {weight}"  )
            # Round to two decimal places
            bmi = "Your BMI is: " + str(round( ((weight) / (height**2)) * 703, 2))
    context = { 
            'bmi': bmi,
            'user_data_form': user_data 
    } 
    return render(request, view, context)


