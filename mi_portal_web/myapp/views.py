from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def services(request):
    return render(request, 'myapp/services.html')

def blog(request):
    return render(request, 'myapp/blog.html')