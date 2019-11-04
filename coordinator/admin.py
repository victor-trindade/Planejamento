from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import User

from import_export.admin import ImportExportModelAdmin
from coordinator.resources import CoordinatorResource, UserResource
from .models import Coordinator


class CoordinatorAdmin(ImportExportModelAdmin):
    resource_class = CoordinatorResource
    pass


class UserAdmin(ImportExportModelAdmin):
    list_display = ('username','email', 'first_name', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    resource_class = UserResource
    pass


admin.site.unregister(User)
admin.site.register(Coordinator,CoordinatorAdmin)
admin.site.register(User, UserAdmin)