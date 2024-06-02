from django.shortcuts import render
from django.http import HttpResponse

import json
import requests
from django.http import JsonResponse



#Create view here

def home(request):
    return render(request, "index.html")


def filter_product_data(products):
    return [
        {
            'title': product['title'],
            'price': product['price'],
            'description': product['description']
        }
        for product in products
    ]


def get_all_products(request):
    #return HttpResponse("get all products reached")
    print("-----------------------------")
    print("sending all products details")
    print("-----------------------------")

    url = "https://fakestoreapi.com/products/"

    # Extract the value associated with the "age" key

    response= requests.get(url)
    products = response.json()


    try:
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()

        print("-----------------------------")
        print("products json= ", products)
        print("-----------------------------")

        # Filter out the required fields
        filtered_products = filter_product_data(products)

    except requests.RequestException as e:
    
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse(filtered_products, safe=False)


def get_product_details(request, id):
    print("-----------------------------")
    print("sending one product details")
    print("-----------------------------")

    print ("ID = ",id)

    url = f"https://fakestoreapi.com/products/{id}"

    print("URL = ",url)

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        filtered_product = filter_product_data([data])

    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse(filtered_product, safe=False)

