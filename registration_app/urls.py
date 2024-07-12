from django.urls import path
from . import views

urlpatterns = [

    path('', views.Registeruser, name='register'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logout, name='logout'),


]
