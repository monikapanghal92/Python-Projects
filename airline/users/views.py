from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
#view for index
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "users/user.html")

#view for login page
def login_view(request):
    if request.method== 'POST':
        username=request.POST["username"]
        password=request.POST["password"]

        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"users/login.html",{"message":"Invalid Credentials"})
    else:
        return render(request,"users/login.html")  

# view for logout page
def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{"message":"Logged Out!"})


 