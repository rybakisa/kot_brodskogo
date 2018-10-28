from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.ReadingsList.as_view(), name='readings-list'),
    path('<slug:slug>', views.ReadingDetail.as_view(), name='reading-details'),

]
