from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from App_general.forms import SubscriptionForm, SubscriptionModelForm
# from App_general.models import Subscription
from .forms import SubscriptionModelForm
from .models import Subscription

# Create your views here.
def homePage(request):
    return render(request, 'App_general/Home.html')

def aboutPage(request):
    return render(request, 'App_general/About.html')

def subcriptionFormPage(request):
    if request.method == 'POST':
        ## print(request.POST)
        #name = request.POST.get('name')
        #email = request.POST.get('email')
        #food_ids = request.POST.getlist('food_ids')
        #new_sub = Subcription()
        #new_sub.name = name
        #new_sub.email = email
        ## new_sub.save()
        ## print(name)
        ## print(email)
        ## print(food_ids)

        # Load Data for Form
        form = SubscriptionModelForm(request.POST)
        if form.is_valid():
            # Use for SubscriptionForm
            # dataForm = form.cleaned_data
            # new_sub = Subscription()
            # new_sub.name = dataForm['name']
            # new_sub.email = dataForm['email']
            # new_sub.save()
            # new_sub.food_set.set(dataForm['food_set'])
            # print(dataForm)

            # Use for SubscriptionModelForm
            form.save()
            return HttpResponseRedirect(reverse('Subscription_ty'))
    else:
        form = SubscriptionModelForm()
    context = {'form':form}
    # menu_Foods = FoodModel.objects.order_by('-is_Premium')
    # context = { 'menuFoods' : menu_Foods}
    return render(request, 'App_general/Subscription_form.html', context)

def subscription_ty(request):
    return render(request, 'App_general/Subscription_ty.html')