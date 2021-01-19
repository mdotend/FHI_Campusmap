from django.db import models
from django.forms import ModelForm
import os

# Create your models here.
class Waypoint(models.Model):
    long = models.FloatField()
    lat = models.FloatField()
    area = models.ForeignKey('Area', on_delete=models.CASCADE, blank=True, null=True)
    plant = models.ForeignKey('PlantType', on_delete=models.CASCADE, blank=True, null=True)


class Area(models.Model):
    name = models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = "Areas"
    def __str__(self):
        return self.name

class PlantType(models.Model):
    marker_dir = os.path.join(os.getcwd(),"fhi/map/static/marker")
    colors = []
    for marker in os.listdir(marker_dir):
        if marker.startswith("marker-icon-") and os.path.isfile(os.path.join(marker_dir, marker)):
            color = marker.split("-")[2].replace(".png","")
            colors.append((color,color.upper()))

    name = models.CharField(max_length=25)
    lat_name = models.CharField(max_length=50, blank=True, null=True)
    wiki = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.CharField(max_length=50,blank=True, null=True)
    marker_color = models.CharField(choices=colors, max_length=10, blank=True, null=True)
    class Meta:
        verbose_name_plural = "PlantTypes"
    def __str__(self):
        return self.name


class WaypointForm(ModelForm):
    class Meta:
        model = Waypoint
        fields = ['long', 'lat', 'plant', 'area']