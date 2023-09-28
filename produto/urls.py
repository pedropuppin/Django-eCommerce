from django.urls import path
from . import views

app_name = 'produto' # ex: produto:list

urlpatterns = [
    path('', views.ProductsList.as_view(), name='list'),
    path('<slug>', views.ProductsDetail.as_view(), name='detail'),
    path('add-to-cart/', views.AddToCart.as_view(), name='add-to-cart'),
    path('remove-from-cart/', views.RemoveFromCart.as_view(), name='remove-from-cart'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('finalize/', views.Finalize.as_view(), name='finalize'),
]
