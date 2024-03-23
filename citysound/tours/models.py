"""Tours models."""

# Django
from django.db import models

class Tour(models.Model):
    """Tour model"""

    name = models.CharField(max_length=300)
    duration = models.PositiveSmallIntegerField(default=1)
    description = models.TextField(blank=True)
    
    photo = models.ImageField(upload_to='tours/photos/')
    audio = models.FileField(upload_to='tours/audios/')


    location = models.CharField(max_length=255)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    is_active = models.BooleanField(
    'active status',
    default=True,
    help_text='Used for disabling the ride or marking it as finished.'
    )

    def __str__(self):
        """Return tour name"""
        return self.name


class Stop(models.Model):
    """Stop model"""

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    audio = models.FileField(upload_to='stops/audios/')
    image = models.ImageField(upload_to='stops/images/')
    description = models.TextField(blank=True)

    def __str__(self):
        """Return stop name"""
        return self.name
        