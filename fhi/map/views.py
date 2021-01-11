from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.template import loader
from django.db.models import Max
from json import dumps

from .models import Waypoint, Area, PlantType

def index(request):
    return HttpResponse("Hello, world. You're at the map index.")


def map(request):
    focus_plants = ""
    try:
        uri,query = request.get_full_path().split("?")
        params = query.split(",")
        for param in params:
            key,value = param.split("=")
            if key == "display" and value:
                focus_plants+=(str(value))+","
    except:
        print("no query")
    waypoints = Waypoint.objects.filter(area__isnull=False)
    plants = Waypoint.objects.filter(plant__isnull=False).select_related('plant')
    template = loader.get_template('map/map.html')
    plantlist = []
    for plant in plants:
        new_plant = {
            'type': str(plant.plant.genus.pk),
            'name': str(plant.plant.genus.name),
            'color': "yellow",
            'lat': plant.lat,
            'long': plant.long
        }
        plantlist.append(new_plant)
    context = {
        'max_area_id': Area.objects.filter().aggregate(Max('pk')).get("pk__max"),
        'max_planttype_id': PlantType.objects.filter().aggregate(Max('pk')).get("pk__max"),
        'waypoint_list': serializers.serialize('json', waypoints),
        'plant_list': dumps(plantlist),
        'focus_plants': str(focus_plants),
    }
    return HttpResponse(template.render(context, request))

def plants(request):
    template = loader.get_template('map/plants.html')
    context = {
        'plant_types': PlantType.objects.all(),
    }
    return HttpResponse(template.render(context, request))
