from django.shortcuts import render
from django.http import HttpResponse

import json
import requests
from django.http import JsonResponse



#Create view here

def index(request):
    return render(request, "home/index.html")
