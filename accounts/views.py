from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
# Create your views here.


def buyersignup(response):
    if response.method == "POST":
        form = BuyerRegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('login')
    else:
        form = BuyerRegisterForm()

    return render(response, "accounts/signup.html", {"form": form})


def sellersignup(response):
    if response.method == "POST":
        form = SellerRegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('login')
    else:
        form = SellerRegisterForm()

    return render(response, "accounts/signup.html", {"form": form})


def redir(response):
    if response.user.is_authenticated and response.user.is_buyer:
        return redirect('bhome')
    else:
        return HttpResponse('<p>Not logged in</p>')
