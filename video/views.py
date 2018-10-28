from django.views import generic
from .models import *


class VideosList(generic.ListView):
    model = Video
    template_name = 'video/videos_list.html'
    context_object_name = 'videos'


class VideoDetail(generic.DetailView):
    model = Video
    template_name = 'video/video_details.html'
    context_object_name = 'video'
