from django.urls import path
from .views import *

app_name = 'accounts_api'

urlpatterns = [
    # path('change-password/<int:id>/', ChangePasswordView.as_view(), name='change-password'),
    path('add-to-wishlist/', AddToWishlist.as_view(), name='add-to-wishlist'),
    path('remove-from-wishlist/', RemoveFromWishlist.as_view(), name='remove-from-wishlist'),
    path('add-to-cart/', AddToCart.as_view(), name='add-to-cart'),
    path('remove-from-cart/', RemoveFromCart.as_view(), name='remove-from-cart'),
]