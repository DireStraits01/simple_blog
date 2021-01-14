from django.urls import path
from . import views

urlpatterns = [
    path('', views.yo_profile, name='yo_profile'),
    path('registration/', views.registr, name='registration'),
    path('register_done/', views.registr, name='register_done'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),



]
