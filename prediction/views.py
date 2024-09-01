# myapp/views.py
from django.shortcuts import render

def index(request):
    # Renders the login page
    return render(request, 'index.html')

def disease(request):
    # Renders the disease selection page
    return render(request, 'disease.html')

def heart(request):
    # Renders the heart disease prediction page
    return render(request, 'heart.html')
