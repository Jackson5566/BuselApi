from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductView.as_view(), name='product'),
    path('product/<int:id>', views.ProductView.as_view(), name='product'),
    path('products', views.ProductsView.as_view(), name='products'),
    path('search-products', views.SearchProductsView.as_view(), name='search_posts'),
]