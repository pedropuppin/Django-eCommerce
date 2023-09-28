from django.db import models
from utils.resize_img import resize_image
from utils.rand_slug import slugify_new


# Create your models here.

class Product(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='produto_img/%Y/%m', blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    price = models.FloatField()
    promo_price = models.FloatField(default=0)
    type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        )
    )    
    
    def get_formated_price(self):
        return f'R$ {self.price:.2f}'.replace('.', ',')
    get_formated_price.short_description = 'Preço'
    
    def get_formated_promo_price(self):
        return f'R$ {self.promo_price:.2f}'.replace('.', ',')
    get_formated_promo_price.short_description = 'Preço Promocional'
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
            
        super().save(*args, **kwargs)
        
        max_image_size = 800
        
        if self.image:
            resize_image(self.image, max_image_size)
            
    
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
    
    def __str__(self):
        return self.name or self.produto.name