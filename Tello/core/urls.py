from django.urls import path
from core.views import *
# from django.contrib.auth.views import LogoutView

app_name = 'core'

urlpatterns = [
    path('',MainPageView.as_view(),name ='main'),
]