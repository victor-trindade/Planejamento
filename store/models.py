from django.db import models
from coordinator.models import Coordinator


class Store(models.Model):
    store_name = models.CharField(verbose_name='Nome da loja', max_length=99)
    store_id = models.CharField(verbose_name='ID da loja', max_length=20)
    visit_day = models.DateField(verbose_name='Dia da visita')
    check_in = models.TimeField()
    check_out =models.TimeField()
    coord_name = models.ForeignKey(Coordinator, on_delete=models.CASCADE, verbose_name='Coordenador')

    def __str__(self):
        return self.store_name
