from django.shortcuts import render,HttpResponse
from pages.models import home_course
# Create your views here.

def index(request):




    return render(request,'cart/cart.html')