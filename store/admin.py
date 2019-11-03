from django.contrib import admin
from import_export.widgets import ForeignKeyWidget

from .models import Store,Coordinator
from import_export import fields, resources
from store.resources import StoreResource
from import_export.admin import ImportExportModelAdmin
# Register your models here.



class StoreAdmin(ImportExportModelAdmin):
    resource_class = StoreResource
    pass
admin.site.register(Store, StoreAdmin)