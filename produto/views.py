from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


# Create your views here.

class ProductsList(View):
    def get(self, *args, **kwargs):
        return HttpResponse('products list')

class ProductsDetail(View):
    def get(self, *args, **kwargs):
        return HttpResponse('products detail')

class AddToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('add to cart')

class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remove from cart')

class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('cart')

class Finalize(View):
    def get(self, *args, **kwargs):
        return HttpResponse('finalize')