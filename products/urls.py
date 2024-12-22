# products/urls.py

from django.urls import path
from . import views

app_name = 'products'  # This is important, makes the 'products' namespace available

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.product_list, name='list'),
    path('about/', views.about, name='about'),
    path('create/', views.product_create, name='create'),
    path('category/<str:category>/', views.product_category, name='category'),
    path('detail/<int:pk>/', views.product_detail, name='detail'),
]
