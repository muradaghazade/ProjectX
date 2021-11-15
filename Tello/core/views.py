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

