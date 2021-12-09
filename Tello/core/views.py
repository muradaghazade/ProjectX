from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView , DetailView , CreateView
from core.models import *
from core.forms import *
from django.views.generic.edit import FormMixin
from django.db.models import Q

class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category__title="Smartphones").order_by('-id')[:4]
        context['accessories'] = Product.objects.filter(~Q(category__title="Smartphones")).order_by('-id')[:4]
        context['images'] = Image.objects.all()
        return context

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'list.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['colors'] = Color.objects.all()
        context['images'] = Image.objects.all()
        return context

    def get_queryset(self):
        title = self.request.GET.get('title')
        brand = self.request.GET.get('brand')
        category = self.request.GET.get('category')
        form_factor = self.request.GET.get('form_factor')
        price = self.request.GET.get('price')
        print(price)
        queryset = Product.objects.order_by('-id')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if brand:
            queryset = queryset.filter(brand__icontains=brand)
        if form_factor:
            queryset = queryset.filter(form_factor=form_factor)
        if category:
            queryset = queryset.filter(category__title=category)

        if price and price == '0-500':
            queryset = queryset.filter(price__gte=0).filter(price__lte=500)
        elif price and price == '500-1000':
            queryset = queryset.filter(price__gte=500).filter(price__lte=1000)
        elif price and price == '1000-2000':
            queryset = queryset.filter(price__gte=1000).filter(price__lte=2000)
        elif price and price == '2000':
            queryset = queryset.filter(price__gte=2000)
            print(queryset)
        
        if brand == "all":
            queryset = Product.objects.order_by('-id')

        if title == 'news':
            queryset = Product.objects.order_by('-id')
        elif title == 'cheap':
            queryset = Product.objects.order_by('price')
        elif title == 'expensive':
            queryset = Product.objects.order_by('-price')
        return queryset

class ProductDetailView(FormMixin, DetailView):
    template_name = 'product.html'
    model = Product
    context_object_name = "product"
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('core:product', kwargs={'slug': self.get_object().slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        context['images'] = Image.objects.filter(product=self.object)[1:]
        context['all_images'] = Image.objects.filter(product=self.object)
        return context

    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if request.method == 'POST':
            if request.user.is_authenticated:
                if form.is_valid():
                    self.form_valid(form)
                    return redirect(reverse_lazy('core:product', kwargs={'slug': self.get_object().slug}))

    def form_valid(self, form):
        form.instance.product = self.get_object()
        form.save()
        return super().form_valid(form)

class FAQView(ListView):
    model = FAQ
    template_name = 'faq.html'
    context_object_name = 'faqs'
    queryset = FAQ.objects.all()