# DeployModel/urls.py
from django.contrib import admin
from django.urls import path
from prediction import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # URL pattern for the login page
    path('disease/', views.disease, name='disease'),  # URL pattern for the disease selection page
    path('heart/', views.heart, name='heart'),  # URL pattern for the heart disease page
]
