from rest_framework import generics
from events.models import Event
from events.serializers import (
    EventCreateSerializer,
    EventListSerializer,
    EventDetailSerializer,
)


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventCreateSerializer


class EventListView(generics.ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
