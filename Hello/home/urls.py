from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("addbook", views.addbook, name='addbook'), 
    path("inventory", views.inventory, name='inventory'),
    path("delete", views.delete, name="delete"),
    path("update", views.update, name="update"),
    path("signup", views.signup, name="signup"),
    path("login", views.handlelogin, name="login"),
    path("logout", views.handlelogout, name="logout")
]