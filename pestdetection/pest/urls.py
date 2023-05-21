from django.contrib import admin
from django.urls import path
from pest import views

urlpatterns = [
   
    path('',views.predict,name='index'),
]