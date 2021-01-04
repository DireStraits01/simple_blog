from django.urls import path
from . import views

urlpatterns = [
    path('prof/', views.yo_profile, name="yo_profile"),
]
