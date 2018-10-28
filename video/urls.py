from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.VideosList.as_view(), name='videos-list'),
    path('<slug:slug>', views.VideoDetail.as_view(), name='video-details'),

]
