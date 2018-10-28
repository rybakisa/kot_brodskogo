from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('videos/', include('video.urls')),
    path('library/', include('library.urls')),
    path('calendar/', include('events_calendar.urls')),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)