from decimal import Context
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from accounts.forms import RegisterForm, LoginForm, CreateOrderForm
from django.views.generic import TemplateView, ListView , DetailView , CreateView, UpdateView
from accounts.models import User, Wishlist, Cart, Order
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic.edit import FormMixin
from .forms import *

def usersignup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            wishlist = Wishlist.objects.create(user=user)
            cart = Cart.objects.create(user=user)
            

            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return render(request, 'index.html')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'index.html')
    else:
        return HttpResponse('Activation link is invalid!')


class LoginUserView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

# class UserProfileView(DetailView):
#     template_name = 'profile-info.html'
#     model = User
#     context_object_name = "user"

class UserProfileView(UpdateView):
    model = User
    template_name = 'profile-info.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('core:index')

    def get_success_url(self):
        return reverse_lazy('account:user-profile', kwargs={'slug':self.get_object().slug})

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.username != self.get_object().username:
            raise PermissionDenied
        return super(UserProfileView, self).dispatch(request, *args, **kwargs)

class UpdatePasswordView(PasswordChangeView):
    template_name = 'reset-password.html'
    form_class = ThePasswordChangeForm
    success_url = reverse_lazy('accounts:login')


class UserWishlistView(DetailView):
    template_name = 'profile-favorites.html'
    context_object_name = "user"
    model = User

class UserCartView(DetailView):
    template_name = 'cart.html'
    context_object_name = "user"
    model = User

class CreateOrderView(FormMixin, DetailView):
    template_name = 'payment-process.html'
    model = User
    context_object_name = "user"
    form_class = CreateOrderForm
    success_url = reverse_lazy('accounts:success')

    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if request.method == 'POST':
            if request.user.is_authenticated:
                if form.is_valid():
                    return self.form_valid(form)

    def form_valid(self, form):
        form.instance.cart = self.request.user.user_cart
        form.instance.final_price = self.request.user.user_cart.get_price_summary()
        form.save()
        for product in self.request.user.user_cart.product_version.all():
            self.request.user.user_cart.product_version.remove(product)
        return super().form_valid(form)

class SuccessPageView(TemplateView):
    template_name = 'success.html'