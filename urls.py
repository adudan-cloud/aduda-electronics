from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reviews/', views.reviews, name='reviews'),
    path('laptop/', views.laptop, name='laptop'),
    path('accessories/', views.accessories, name='accessories'),  
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('laptop/', views.laptop_list, name='laptop_list'),
    path('laptop/', views.index, name='index'),
    path('accessories/<str:brand>/', views.accessories_by_brand, name='accessories_by_brand'),
]





