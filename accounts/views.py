from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages 
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect #used to redirect from same page

from django.contrib.auth import authenticate,login,logout



# Create your views here.

def login_page(request):
    #return HttpResponse("login page reached")
     if request.method=="POST":
        first_name = request.POST.get("first_name")
        last_name =  request.POST.get("last_name")
        email =  request.POST.get("email")
        password =  request.POST.get("password")
        user_obj = User.objects.filter(username = email) 

        if not user_obj.exists():
            #print(" email already registered ", email)
            messages.warning( request, 'Account not found' ) 
            return HttpResponseRedirect(request.path_info)

        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, "Your Account not Verified, check verification link on email")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username=email,password=password) #checks if user/password exists or not
        if user_obj:
            login(request, user_obj)
            return redirect("/")

        messages.warning(request, "Invalid credentials")
        return HttpResponseRedirect(request.path_info)


        return render(request, "accounts/login.html")

def register_page(request):

    if request.method=="POST":
        first_name = request.POST.get("first_name")
        last_name =  request.POST.get("last_name")
        email =  request.POST.get("email")
        password =  request.POST.get("password")
        user_obj = User.objects.filter(username = email) 

        if user_obj.exists():
            print(" email already registered ", email)
            messages.warning( request, 'Email is already registered' ) 
            return HttpResponseRedirect(request.path_info)

        #print ("first_name=",first_name,"last name = ",last_name,"email=",email)

        user_obj= User.objects.create(first_name= first_name,last_name=last_name,email=email,username=email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'Please check your email for the registration link')
        return HttpResponseRedirect(request.path_info)

    return render(request, "accounts/register.html")