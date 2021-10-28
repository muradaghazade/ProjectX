from django.shortcuts import render
from django.views.generic import TemplateView, ListView , DetailView , CreateView
from core.models import *
from django.db.models import Q

class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category__title="Smartphones").order_by('-id')
        context['accessories'] = Product.objects.filter(~Q(category__title="Smartphones")).order_by('-id')
        context['images'] = Image.objects.all()
        return context

class ProductListView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.order_by('-id')
        context['images'] = Image.objects.all()
        return context

class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        context['images'] = Image.objects.filter(product=self.object)[1:]
        context['all_images'] = Image.objects.filter(product=self.object)
        return context

