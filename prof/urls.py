from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.profilePage, name='profilePage'),
    path('register/', views.register, name='register'),
    path('register_done/', views.register, name='register_done'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),



]
