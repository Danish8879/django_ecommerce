from django.shortcuts import render
from products.models import Product


# Create your views here.


def get_product(request, slug):

    try:
        product = Product.objects.get(slug = slug)
        context = {"product":product}
        return render(request, "product/product.html", context= context )

    except Exception as e:
        print ("----------------------------------")
        print ("Get Product exception: ", e)
        print ("----------------------------------")
        
