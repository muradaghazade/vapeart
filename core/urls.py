from django.urls import path
from .views import *


app_name = 'core'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('brands/', BrandsView.as_view(), name='brands'),
    path('shipping/', ShippingView.as_view(), name='shipping'),

]