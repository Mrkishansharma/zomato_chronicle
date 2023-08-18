# zomato/views.py

from django.shortcuts import render, redirect
from .menu import get_menu
from .forms import AddDishForm

def display_menu(request):
    menu = get_menu()
    return render(request, 'templates/zomato/menu.html', {'menu': menu})




def add_dish(request):
    if request.method == 'POST':
        form = AddDishForm(request.POST)
        if form.is_valid():
            menu = get_menu()
            dish_id = len(menu) + 1
            menu[dish_id] = {
                'name': form.cleaned_data['name'],
                'price': form.cleaned_data['price'],
                'available': form.cleaned_data['available'],
            }
            return redirect('display_menu')
    else:
        form = AddDishForm()
    
    return render(request, 'zomato/add_dish.html', {'form': form})