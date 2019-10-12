from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dine_info/', views.dine_info, name='dine_info'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('Order', views.food_order, name='food_order'),


]