from django.urls import path
from .views import CoordinatorDetail

urlpatterns = [
    path('<int:pk>', CoordinatorDetail.as_view(),name='coord_detail'),
]
