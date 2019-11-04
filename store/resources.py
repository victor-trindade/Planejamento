from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from coordinator.models import Coordinator
from .models import Store

class StoreResource(resources.ModelResource):

    coordinator = fields.Field (
        column_name = 'Nome Coord',
        attribute = 'coordinator' ,
        widget = ForeignKeyWidget(Coordinator , 'name'))

    name = fields.Field(
        column_name = 'Nome Loja',
        attribute = 'name')

    id_sf = fields.Field(
        column_name = 'ID Loja',
        attribute = 'id_sf')

    visit_day = fields.Field(
        column_name = 'Dia Visita',
        attribute = 'visit_day')

    check_in = fields.Field(
        column_name = 'Hora Entrada',
        attribute = 'check_in')

    check_out = fields.Field(
        column_name = 'Hora Saida',
        attribute = 'check_out')

    class Meta:
        model = Store
