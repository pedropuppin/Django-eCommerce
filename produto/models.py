from django.db import models
from utils.resize_img import resize_image


# Create your models here.

class Product(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='produto_img/%Y/%m', blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.FloatField()
    promo_price = models.FloatField(default=0)
    type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Vestuário'),
            ('A', 'Acessório'),
        )
    )    
        
    def save(self, *args, **kwargs):
    
        max_image_size = 800
        
        if self.image:
            resize_image(self.image, max_image_size)
            
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    
class Variation(models.Model):
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
        
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField()
    promo_price = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)
    slug = models.SlugField(max_length=100, blank=True)
    
    
    def __str__(self):
        return self.name or self.produto.name