from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, UnicodeUsernameValidator
from core.common import slugify
from .managers import UserManager
from core.models import Product, ProductVersion
# from django.core.mail import send_mail

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator
    username = models.CharField(
        ('username'),
        max_length=150,
        blank=True,
        null=True,
        unique=False,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    email = models.EmailField(('email adress'), unique=True)
    full_name = models.CharField(max_length=100)
    number = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.email}"

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        self.slug = f'{slugify(self.full_name)}-{self.id}'
        super(User, self).save(*args, **kwargs)


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True, related_name='user_wishlist')
    product = models.ManyToManyField(Product, verbose_name=("Product"), db_index=True, related_name='wishlist_product', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def __str__(self):
        return f"{self.user.email}'s Wishlist"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True, related_name='user_cart')
    product_version = models.ManyToManyField(ProductVersion, verbose_name=("Product Version"), db_index=True, related_name='cart_product', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
    
    def __str__(self):
        return f"{self.user.email}'s Cart"

    def get_price_summary(self):
        price = 0
        for product in self.product_version.all():
            price += product.product.price
        return price

class Order(models.Model):
    PAYMENT_CHOICES = (
    ("Onlayn kart ilə ödəmə", ("Onlayn kart ilə ödəmə")),
    ("Qapıda nağd ödəmə", ("Qapıda nağd ödəmə"))
)
    customer_name = models.CharField(max_length=100)
    customer_surname = models.CharField(max_length=100)
    customer_number = models.CharField(max_length=100)
    customer_adress = models.CharField(max_length=1000)
    customer_home_number = models.CharField(max_length=50)
    message_for_courier = models.TextField('Message for courier')
    payment_type = models.CharField(choices=PAYMENT_CHOICES, max_length=6000)
    customer_email = models.EmailField(('Email adress'), unique=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, db_index=True, related_name='cart_order', null=True, blank=True)
    final_price = models.IntegerField('Final price',blank=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Sifarişçi: {self.customer_name} {self.customer_surname}  Məbləğ: {self.final_price} AZN"
