from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from coordinator.models import Coordinator
from .models import Store

class StoreResource(resources.ModelResource):
    coordinator = fields.Field (
        column_name = 'coordinator',
        attribute = 'coordinator' ,
        widget = ForeignKeyWidget(Coordinator , 'name'))

    class Meta:
        model = Store
