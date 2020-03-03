from rest_framework import serializers, viewsets
from .models import Room, RoomDirection

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('name',)

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomDirectionSerializer(serializers.HyperlinkedModelSerializer):
    starting_room = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = RoomDirection
        fields = ('starting_room', 'ending_room', 'direction')

class RoomDirectionViewSet(viewsets.ModelViewSet):
    serializer_class = RoomDirectionSerializer
    queryset = RoomDirection.objects.all()