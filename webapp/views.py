from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Products
from .forms import NewProductForm

def homepage_view(request):
    form = NewProductForm()

    if request.method == 'POST':
        form = NewProductForm(request.POST)

        if form.is_valid():
            form.save()

            messages.info(request, 'Product added successfully!')
            return redirect('homepage')
                

    products = Products.objects.all().order_by('name')
    context = {'form': form,'products': products}
    return render(request, 'app/homepage.html', context)