from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Area, Waypoint, PlantType

# Register your models here.
admin.site.register(Area)
admin.site.register(Waypoint, LeafletGeoAdmin)
admin.site.register(PlantType)