from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def home(request):
    messages.success(request, 'Hello welcome here you can accurate your home values')
    return render(request, 'HousePrice/home.html')