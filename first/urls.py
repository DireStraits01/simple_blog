from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.home, name='admin'),
    path('', views.home, name='home'),
    path('<int:id>', views.artical_page, name='artical_page'),
    path('add-article/', views.add_article, name='add_article'),
    path('update-post/<int:id>/', views.update_post, name='update_post'),
    path('like/<int:pk>/', views.likes_post, name='likes_post'),

]
