from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.

class Checkout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('checkout')

class CloseOrder(View):
    def get(self, *args, **kwargs):
        return HttpResponse('closer order')

class Detail(View):
    def get(self, *args, **kwargs):
        return HttpResponse('detail')