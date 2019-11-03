from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from store.models import Store
from django.views.generic.dates import MonthArchiveView,WeekArchiveView


class MonthArchiveViewPage(MonthArchiveView):


    template_name = 'home/month_archive.html'
    date_field = "visit_day"
    allow_future = True
    def get_queryset(self,  **kwargs):
        fullname = self.request.user.get_full_name()
        return Store.objects.filter(coordinator__name=fullname.upper()).order_by('coordinator__name','-visit_day')

class WeekArchiveViewPage(WeekArchiveView):

    queryset = Store.objects.all()
    template_name = 'home/week_archive.html'
    date_field = "visit_day"
    week_format = "%W"
    allow_future = True

