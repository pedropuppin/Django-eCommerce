from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.validate_cpf import valida_cpf
import re

# Create your models here.

class Profile(models.Model):
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    cpf = models.CharField(
        max_length=11, 
        help_text='Informe seu CPF sem pontos ou traços'
    )
    address = models.CharField(max_length=50)
    num = models.CharField(max_length=5)
    complement = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=30)
    state = models.CharField(
        max_length=2,
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def clean(self):
        error_messages = {}
        
        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Informe um CPF válido'
            
        if not re.search(r'^[0-9]', self.cep) or len(self.cep) != 8:
            error_messages['cep'] = 'CEP inválido, digite os 8 números do CEP'
        
        if error_messages:
            raise ValidationError(error_messages)
    
