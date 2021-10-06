from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('login',views.loginUser),
    path('signup',views.signUp),
    path('about',views.about),
    path('contact',views.contact),
    path('services',views.services),

]