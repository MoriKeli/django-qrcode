from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Products


def homepage_view(request):
    

    context = {'products': products}
    return render(request, 'app/homepage.html', context)