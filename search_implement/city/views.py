from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import City
from django.db.models import Q

class Hv(TemplateView):
    template_name = 'home.html'

class Sv(ListView):
    model =  City
    template_name = 'search.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =City.objects.filter(
        Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list


