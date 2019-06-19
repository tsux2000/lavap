from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
# from .models import *
# from .forms import *
import hashlib,json
from decimal import Decimal
import datetime

class MapView(TemplateView):
    def get(self, request):
        params = {
            'meta': {'title': 'Lavap'}
        }
        return render(request, 'main/index.html', params)

class LavatoryView(TemplateView):
    def get(self, request):
        params = {}
        return render(request, 'main/lavatory.html', params)
    def post(self, request):
        params = {}
        return render(request, 'main/lavatory.html', params)
