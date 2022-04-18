from django.urls import path
from .views import *

app_name = 'core_api'

urlpatterns = [
    path('products/', ProductsAPIView.as_view(), name='create-product-version'),
    
]