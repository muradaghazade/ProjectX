from django.urls import path
from .views import *

app_name = 'core_api'

urlpatterns = [
    path('create-product-version/', ProductVersionAPIView.as_view(), name='create-product-version'),
    
]