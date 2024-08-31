from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('disease/', views.disease, name='disease'),
    path('heart/', views.heart, name='heart'),
]
