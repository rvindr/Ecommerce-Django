from django.shortcuts import render, redirect
from item.models import category, Item
from .forms import SignupForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = category.objects.all()
    return render(request,'core/index.html',{
        'categories':categories, 
        "items":items
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        # print('inside the post')
        form = SignupForm(request.POST)
        # print('ejkwndw')

        if form.is_valid():
            print('inside valid')
            form.save()
            return redirect('/login/')
        else:
            form = SignupForm()

    form = SignupForm()
    return render(request,'core/signup.html',{
        'form':form
    })
