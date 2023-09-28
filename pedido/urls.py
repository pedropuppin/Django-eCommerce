from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.Checkout.as_view(), name='checkout'),
    path('close-order/', views.CloseOrder.as_view(), name='close-order'),
    path('detail/', views.Detail.as_view(), name='detail'),
]
