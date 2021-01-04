from django.db import models

# Create your models here.
class Waypoint(models.Model):
    long = models.FloatField()
    lat = models.FloatField()
    area = models.ForeignKey('Area', on_delete=models.CASCADE, blank=True, null=True)
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)

class Area(models.Model):
    name = models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = "Areas"
    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(max_length=25)
    genus = models.ForeignKey('PlantType', on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Plants"
    def __str__(self):
        return self.name

class PlantType(models.Model):
    name = models.CharField(max_length=25)
    lat_name = models.CharField(max_length=50, blank=True, null=True)
    wiki = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.CharField(max_length=50,blank=True, null=True)
    class Meta:
        verbose_name_plural = "PlantTypes"
    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title