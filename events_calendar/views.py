from django.views import generic
from .models import *


class CalendarView(generic.TemplateView):
    template_name = 'events_calendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['calendar'] = Calendar.objects.all()[0]
        return context
