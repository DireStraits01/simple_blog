from django.urls import path
from . import views

urlpatterns = [
    path('', views.yo_profile, name='yo_profile'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),

]
