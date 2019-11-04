from django.contrib.auth.hashers import make_password
from import_export import resources, fields
from .models import Coordinator
from django.contrib.auth.models import User

class CoordinatorResource(resources.ModelResource):

    class Meta:
        model = Coordinator

class UserResource(resources.ModelResource):

    class Meta:
        model = User

    def before_import_row(self, row, **kwargs):
        self.password = row.get('password')
        row['password'] = make_password(self.password)

