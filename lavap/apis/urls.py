from rest_framework import routers
from django.urls import path
from .views import *

# router = routers.DefaultRouter()
# router.register(r'lavatories', LavatoryViewSet)

urlpatterns = [
    path('lavatory/<int:pk>/', lavatory_detail),
    path('lat/<lat>/lng/<lng>/', lavatories_list),
]
