from django.urls import path
from .views import MonthArchiveViewPage, WeekArchiveViewPage


urlpatterns = [
    path('<int:year>/<int:month>/', MonthArchiveViewPage.as_view(month_format='%m'), name="archive_month"),
    path('week/<int:year>/<int:week>/', WeekArchiveViewPage.as_view(), name="archive_week"),

]
