from django.urls import path
from . import views

urlpatterns = [
    path('', views.yo_profile, name='yo_profile'),
    path('login_page/', views.login_page, name='login_page'),
    path('registration_page/', views.registration_page,
         name='registration_page'),
]
