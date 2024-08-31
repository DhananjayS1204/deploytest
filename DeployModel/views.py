import joblib
from django.shortcuts import render


def result(request):
    rfc = joblib.load('heart.joblib')

