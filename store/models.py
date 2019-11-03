from django.db import models
from import_export.widgets import ForeignKeyWidget

from coordinator.models import Coordinator
from import_export import resources, fields


class Store(models.Model):
    name = models.CharField(verbose_name='Nome da Loja',max_length=99)
    id_sf = models.CharField(verbose_name= 'ID da loja',max_length=18) #id Salesforce da loja
    visit_day = models.DateField(verbose_name='Dia da Visita')
    check_in = models.TimeField(verbose_name='Hora da entrada')
    check_out = models.TimeField(verbose_name='Hora da saída')
    coordinator = models.ForeignKey(Coordinator,on_delete=models.CASCADE,verbose_name='Coordenador')

    def __str__(self):
        return self.name

#Class for django-import-export
# class StoreResource(resources.ModelResource):
#     coordinator_name = fields.Field(
#         column_name='coordinator_name',
#         attribute='coordinator',
#         widget=ForeignKeyWidget(Coordinator, 'name'))
#
#     class Meta:
#         model = Coordinator