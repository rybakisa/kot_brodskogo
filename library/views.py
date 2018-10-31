from django.views import generic
from .models import *


class ReadingsList(generic.ListView):
    model = ReadingMaterial
    template_name = 'library/readings_list.pug'
    context_object_name = 'readings'


class ReadingDetail(generic.DetailView):
    model = ReadingMaterial
    template_name = 'library/reading_details.html'
    context_object_name = 'reading'
