from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from store.models import Store
from django.views.generic.dates import MonthArchiveView, WeekArchiveView, TodayArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
    template_name = 'home/home.html'

class StoreMonthArchiveView(MonthArchiveView):


    template_name = 'home/month_archive.html'
    date_field = "visit_day"
    allow_future = True
    def get_queryset(self,  **kwargs):
        if self.request.user.is_authenticated:
            fullname = self.request.user.get_full_name()
            return Store.objects.filter(coordinator__name=fullname.upper()).order_by('coordinator__name','-visit_day')
        else:
            return Store.objects.all()

class StoreWeekArchiveView(WeekArchiveView):

    queryset = Store.objects.all()
    template_name = 'home/week_archive.html'
    date_field = "visit_day"
    week_format = "%W"
    allow_future = True




class StoreTodayArchiveView(LoginRequiredMixin, TodayArchiveView):
    def get_queryset(self,  **kwargs):
        if self.request.user.is_authenticated:
            fullname = self.request.user.get_full_name()
            return Store.objects.filter(coordinator__name=fullname.upper()).order_by('coordinator__name','-visit_day')

    template_name = 'home/day_archive.html'
    date_field = "visit_day"
    allow_future = True