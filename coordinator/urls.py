from django.contrib import admin
from django.urls import path, include
from coordinator.views import meu_ovo
urlpatterns = [
    path('ovo/', meu_ovo),
]