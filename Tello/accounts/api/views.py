from rest_framework import generics
from rest_framework.response import Response
# from django.contrib.auth.models import User
from rest_framework.views import APIView
from . import serializers
from rest_framework.permissions import IsAuthenticated   
from rest_framework.generics import UpdateAPIView
from .serializers import ChangePasswordSerializer
from rest_framework import status
from core.models import Product, ProductVersion
from accounts.models import User

class AddToWishlist(APIView):
    def post(self, request, *args, **kwargs):
        product_id = self.request.data.get('product')
        user_id = self.request.data.get('user')
        product = Product.objects.get(pk=int(product_id))
        user = User.objects.get(pk=int(user_id))
        user.user_wishlist.product.add(product)
        return Response("Added to Wishlist")

class RemoveFromWishlist(APIView):
    def post(self, request, *args, **kwargs):
        product_id = self.request.data.get('product')
        user_id = self.request.data.get('user')
        product = Product.objects.get(pk=int(product_id))
        user = User.objects.get(pk=int(user_id))
        user.user_wishlist.product.remove(product)
        return Response("Removed from Wishlist")

class AddToCart(APIView):
    def post(self, request, *args, **kwargs):
        product_id = self.request.data.get('product')
        user_id = self.request.data.get('user')
        product = ProductVersion.objects.get(pk=int(product_id))
        user = User.objects.get(pk=int(user_id))
        user.user_cart.product_version.add(product)
        return Response("Added to Cart")

class RemoveFromCart(APIView):
    def post(self, request, *args, **kwargs):
        product_id = self.request.data.get('product')
        user_id = self.request.data.get('user')
        product = ProductVersion.objects.get(pk=int(product_id))
        user = User.objects.get(pk=int(user_id))
        user.user_cart.product_version.remove(product)
        return Response("Removed from Cart")