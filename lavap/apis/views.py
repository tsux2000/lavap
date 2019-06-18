import django_filters
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Lavatory
from .serializer import LavatorySerializer
from decimal import *

@csrf_exempt
def lavatories_list(request, lat, lng):
    """
    List up near lavatories, or create a new lavatory.
    """

    lat = Decimal(int(lat) / 1000000).quantize(Decimal("0.000001"),rounding=ROUND_HALF_UP)
    lng = Decimal(int(lng) / 1000000).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
    DIFF_LAT = Decimal(0.009013).quantize(Decimal("0.000001"),rounding=ROUND_HALF_UP)
    DIFF_LNG = Decimal(0.010966).quantize(Decimal("0.000001"),rounding=ROUND_HALF_UP)
    if request.method == 'GET':
        lava = Lavatory.objects.filter(lat__range=(float(lat - DIFF_LAT), float(lat + DIFF_LAT)), lng__range=(float(lng - DIFF_LNG), float(lng + DIFF_LNG))).values()[:20]
        lavas = list(lava[:])
        k = 1
        while True:
            flg = 0
            for i in range(len(lavas) - k):
                span = (lavas[i]['lat']-lat)**2 + (lavas[i]['lng']-lng)**2
                next_span = (lavas[i+1]['lat']-lat)**2 + (lavas[i+1]['lng']-lng)**2
                if span > next_span:
                    save = lavas[i]
                    lavas[i] = lavas[i+1]
                    lavas[i+1] = save
                    flg = 1
            k += 1
            if flg:
                continue
            break
        return JsonResponse(lavas, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        seri = LavatorySerializer(data=data)
        if seri.is_valid():
            seri.save()
            return JsonResponse(seri.data, status=201)
        return JsonResponse(seri.errors, status=400)

@csrf_exempt
def lavatory_detail(request, pk):
    """
    Retrieve, update or delete a lavatory.
    """
    try:
        lava = Lavatory.objects.get(pk=pk)
    except Lavatory.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        seri = LavatorySerializer(lava)
        return JsonResponse(seri.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        seri = LavatorySerializer(lava, data=data)
        if seri.is_valid():
            seri.save()
            return JsonResponse(seri.data)
        return JsonResponse(seri.errors, status=400)

    elif request.method == 'DELETE':
        lava.delete()
        return HttpResponse(status=204)
