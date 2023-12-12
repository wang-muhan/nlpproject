from django.shortcuts import render

# Create your views here.

def dialog(request):
    return render(request, "dialog.html", {"hello":"hello world"})