from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
import django
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['POST'])
def login(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request,user)
            # Redirect to a success page.
            return HttpResponse(status=200)
        else:
            # Return an 'invalid login' error message.
            return HttpResponse(status=401)
    return HttpResponse(status=400)
    
def register(request):
    return render(request, "account/register.html")