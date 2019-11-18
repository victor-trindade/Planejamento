from django.urls import path
from .views import StoreMonthArchiveView, StoreWeekArchiveView,StoreTodayArchiveView, HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('<int:year>/<int:month>/', StoreMonthArchiveView.as_view(month_format='%m'), name="archive_month"),
    path('week/<int:year>/<int:week>/', StoreWeekArchiveView.as_view(), name="archive_week"),
    path('today/', StoreTodayArchiveView.as_view(), name="archive_today"),

]
