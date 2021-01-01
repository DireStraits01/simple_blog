from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.home, name='admin'),
    path('', views.home, name='home'),
    path('<int:id>', views.artical_page, name='artical_page'),
    path('add_article/', views.add_article, name='add_article')
]
