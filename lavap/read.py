import json
from decimal import *
from apis.models import Lavatory

f = open('doc.json', 'r')
datalist = json.load(f)
f.close()

for i in datalist:
    lat = Decimal(i['lat']).quantize(Decimal("0.000001"),rounding=ROUND_HALF_UP)
    lng = Decimal(i['lng']).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
    l = Lavatory(lat=lat, lng=lng, building_name=i['name'])
    l.save()
