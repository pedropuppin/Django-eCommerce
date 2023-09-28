from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        max_length=1,
        default='C',
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('O', 'Concluído'),
            ('X', 'Cancelado'),
        )
    )
    
    def __str__(self):
        return f'Pedido nº {self.pk}'
     
     
class OrderItem(models.Model):
    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'
        
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=50)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    promo_price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField()
    image = models.CharField(max_length=2000)
    
    def __str__(self):
        return f'Item do pedido nº {self.order.pk}'