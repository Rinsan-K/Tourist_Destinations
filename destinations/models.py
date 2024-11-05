from django.db import models

# Create your models here.

from django.db import models

class TouristDestination(models.Model):
    place_name = models.CharField(max_length=255)
    weather = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100)
    location_district = models.CharField(max_length=100)
    google_map_link = models.URLField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='destination_images/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.place_name
