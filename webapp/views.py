from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # return redirect(restaurant_home)
    return render(request, 'index.html', {})

@login_required(login_url='/restaurant/sign-in')
def restaurant_home(request):
    return render(request, 'restaurant/base.html', {})

@login_required(login_url='/restaurant/sign-in')
def restaurant_account(request):
    return render(request, 'restaurant/account.html', {})

@login_required(login_url='/restaurant/sign-in')
def restaurant_meal(request):
    return render(request, 'restaurant/meal.html', {})

@login_required(login_url='/restaurant/sign-in')
def restaurant_order(request):
    return render(request, 'restaurant/order.html', {})

@login_required(login_url='/restaurant/sign-in')
def restaurant_report(request):
    return render(request, 'restaurant/report.html', {})

def restaurant_sign_up(request):
    return render(request, 'restaurant/sign_up.html', {
        "user_form": user_form,
        "restaurant_form": restaurant_form
    })

