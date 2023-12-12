from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
import django
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request,user)
            # Redirect to a success page.
            return HttpResponse("Success!")
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("Fail!, username is "+username + password)
    return render(request, 'account/login.html')
    
def register(request):
    return render(request, "account/register.html")