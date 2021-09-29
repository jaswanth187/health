from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index),
    path('login',views.loginUser),
    path('signup',views.signUp),
]