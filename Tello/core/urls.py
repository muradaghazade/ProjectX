from django.urls import path
from core.views import *
# from django.contrib.auth.views import LogoutView

app_name = 'core'

urlpatterns = [
    path('',MainPageView.as_view(),name ='main'),
    path('products/',ProductListView.as_view(),name ='products'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product'),
    path('faq/', FAQView.as_view(), name='faq'),
]