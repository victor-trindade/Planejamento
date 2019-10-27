from django.db import models

# Create your models here.

class Coordinator(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=80)
    id_sf = models.CharField(verbose_name='ID Salesforce', max_length=18) #id Salesforce

    def __str__(self):
        return self.name