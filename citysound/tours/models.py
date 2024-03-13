"""Tours models."""

# Django
from django.db import models

class Tour(models.Model):
    """Tour model"""

    name = models.CharField(max_length=300)
    duration = models.PositiveSmallIntegerField(default=1)
    description = models.TextField(blank=True)
    
    photo = models.ImageField(upload_to='photos/')
    audio = models.FileField(upload_to='audio/')


    location = models.CharField(max_length=255)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    is_active = models.BooleanField(
    'active status',
    default=True,
    help_text='Used for disabling the ride or marking it as finished.'
    )
