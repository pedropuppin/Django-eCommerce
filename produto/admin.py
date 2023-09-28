from django.contrib import admin
from .models import Product, Variation

# Register your models here.

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'promo_price', 'type')
    list_display_links = ('name',)
    search_fields = ('id', 'name', 'slug')
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('name',),
    }
    inlines = VariationInline,
    
@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ('produto', 'name', 'price', 'promo_price', 'stock')