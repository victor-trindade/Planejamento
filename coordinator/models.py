from django.db import models


class Coordinator(models.Model):
    coord_name = models.CharField(max_length=50)
    coord_id = models.CharField(max_length=20)


    def __str__(self):
        return self.coord_name