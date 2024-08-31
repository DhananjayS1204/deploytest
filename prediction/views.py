from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def disease(request):
    return render(request, 'disease.html')

def heart(request):
    return render(request, 'heart.html')