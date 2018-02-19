from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, View

from bs4 import BeautifulSoup
import requests

from .models import Shop


class ShopListView(ListView):
    model = Shop
    template_name = 'list.html'
    context_object_name = 'shops'

    def get_queryset(self):
        queryset = Shop.objects.filter(opened=True).order_by('stars', 'name')
        return queryset


class CalculateView(View):

    def get(self, request, *args, **kwargs):
        shops = Shop.objects.filter(opened=True, stars=self.kwargs['stars'], checked=False)
        for shop in shops:
            req = requests.get(shop.url)
            status_code = req.status_code

            if status_code == 200:
                html = BeautifulSoup(req.text)
                stars = html.find_all('img', {'alt': '*'})
                shop.stars = stars.__len__()
                shop.checked = True
                shop.save()
            else:
                shop.error = True
                shop.save()

        return HttpResponseRedirect('/')


class ResetView(View):
    def get(self, request, *args, **kwargs):
        shops = Shop.objects.filter(opened=True)
        for shop in shops:
            shop.checked = False
            shop.save()
