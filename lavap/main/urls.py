from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', MapView.as_view(), name='index'),
    path('lavatory/<int:lava_id>', LavatoryView.as_view(), name='lava'),
]

