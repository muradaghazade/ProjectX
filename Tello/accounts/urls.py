from django.urls import path
from core.views import *
from accounts.views import *
from django.contrib.auth.views import LogoutView

app_name = 'account'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/<slug:slug>/', UserProfileView.as_view(), name='user-profile'),
    path('change-password/', UpdatePasswordView.as_view(), name='change-password'),
    path('wishlist/<slug:slug>/', UserWishlistView.as_view(), name='profile-favorites'),
    path('cart/<slug:slug>/', UserCartView.as_view(), name='cart'),
    path('create-order/<slug:slug>/', CreateOrderView.as_view(), name='create-order'),
    path('success/', SuccessPageView.as_view() ,name ='success'),
    path('register/', usersignup,name ='register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate_account, name='activate'),
    path('log-out', LogoutView.as_view(), name='log-out'),
]