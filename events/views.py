from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from events.models import Event, VisitEvent, Status
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

    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            data = {'error': "event doesn't exist"}
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        event_serializer = EventDetailSerializer(event, context={'request': request})

        if not VisitEvent.objects.filter(user_id=request.user, event_id=event).exists():
            VisitEvent.objects.create(
                user_id=request.user,
                event_id=event,
                status_id=Status.objects.get(status_name='not selected')
            )
        return Response(event_serializer.data)
