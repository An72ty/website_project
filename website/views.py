from django.shortcuts import render
from django.views.generic import TemplateView
from .utils import nav_elements


class Index(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['nav_elements'] = nav_elements
        context['page_number'] = 0

        return context


class InterestingPlaces(TemplateView):
    template_name = 'website/interesting_places.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['nav_elements'] = nav_elements
        context['page_number'] = 1

        return context


class History(TemplateView):
    template_name = 'website/history.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['nav_elements'] = nav_elements
        context['page_number'] = 2

        return context


class News(TemplateView):
    template_name = 'website/news.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['nav_elements'] = nav_elements
        context['page_number'] = 3

        return context
