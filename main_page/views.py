from django.views import generic
from .models import *


class IndexView(generic.TemplateView):
    template_name = 'main_page/main.pug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scenes'] = Scene.objects.all().order_by('number')
        context['social_medias'] = SocialMedia.objects.all()
        return context
