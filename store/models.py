from django.db import models
from coordinator.models import Coordinator

class Store(models.Model):
    name = models.CharField(verbose_name='Nome da Loja',max_length=99)
    id_sf = models.CharField(verbose_name= 'ID da loja',max_length=18) #id Salesforce da loja
    visit_day = models.DateField(verbose_name='Dia da Visita')
    check_in = models.TimeField(verbose_name='Hora da entrada')
    check_out = models.TimeField(verbose_name='Hora da saída')
    coordinator = models.ForeignKey(Coordinator,on_delete=models.CASCADE,verbose_name='Coordenador')