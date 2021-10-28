from django.urls import path
from core.views import *
from accounts.views import *
from django.contrib.auth.views import LogoutView

app_name = 'account'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', usersignup,name ='register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate_account, name='activate'),
    path('log-out', LogoutView.as_view(), name='log-out'),
]