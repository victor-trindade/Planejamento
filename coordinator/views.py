from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Coordinator


class CoordinatorDetail(DetailView):
    model = Coordinator
