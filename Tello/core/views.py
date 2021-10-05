from django.shortcuts import render
from django.views.generic import TemplateView, ListView , DetailView , CreateView

class MainPageView(TemplateView):
    template_name = 'index.html'
