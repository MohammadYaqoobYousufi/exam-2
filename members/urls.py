from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.BlogPost, name='product_list.html'),
    path('members/', views.products, name='product_list.html'),
]