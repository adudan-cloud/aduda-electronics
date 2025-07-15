from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Laptop,Accessory

from django.shortcuts import render

def home(request):
    return render(request, 'laptop/home.html')

def about(request):
    return render(request,'laptop/about.html')

def reviews(request):
    return render(request,'laptop/reviews.html')

def laptop(request):
    return render(request, 'laptop/laptop.html')

def accessories(request):
    return render(request,'laptop/accessories.html')

def contact(request):
    return render( request,'laptop/contact.html')

def login_register(request):
    return render(request,'laptop/login_register html')
def laptop_list(request):
    return render(request, 'laptop/list.html')
def accessories_by_brand(request, brand):
    return render(request, 'accessories/brand.html', {'brand': brand})
def index(request):
    return render(request, 'laptop/index.html')

