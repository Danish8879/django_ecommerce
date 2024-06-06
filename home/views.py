from django.shortcuts import render

from products.models import Product

#Create view here

def index(request):

    products = Product.objects.all()

    context = { 'products' : products,}

    return render(request, "home/index.html",context)
