from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)

class RoomDirection(models.Model):
    class Meta:
        unique_together = ('starting_room', 'ending_room', 'direction')
    class Directions(models.TextChoices):
        NORTH = 'N', _('North')
        SOUTH = 'S', _('South')
        EAST = 'E', _('East')
        WEST = 'W', _('West')
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    starting_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="starting_room")
    ending_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="ending_room")
    direction = models.CharField(max_length=1, choices=Directions.choices)
    