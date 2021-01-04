from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Area, Waypoint, Plant, PlantType

# Register your models here.
admin.site.register(Area)
admin.site.register(Waypoint, LeafletGeoAdmin)
admin.site.register(Plant)
admin.site.register(PlantType)