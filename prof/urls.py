from django.urls import path
from . import views

urlpatterns = [
    path('', views.yo_profile, name='yo_profile'),
    path('register/', views.register, name='register'),
    path('register_done/', views.register, name='register_done'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),



]
