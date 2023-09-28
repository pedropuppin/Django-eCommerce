from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'status')
    list_display_links = ('user',)
    search_fields = ('id', 'user')
    list_per_page = 10
    ordering = '-id',
    inlines = OrderItemInline,

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'variation', 'price', 'promo_price', 'quantity')
    list_display_links = ('order',)
    search_fields = ('id', 'order')
    list_per_page = 10
    ordering = '-id',