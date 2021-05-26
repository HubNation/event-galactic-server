from rest_framework import serializers
from django.contrib.auth import get_user_model
from events.models import (
    Event, EventCategory, EventMedia,
    Type, Category, VisitEvent,
)

User = get_user_model()


class VisitEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitEvent
        fields = ('status_id',)


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date_event', 'time_event', 'interval_time', 'place')


class EventDetailSerializer(serializers.ModelSerializer):
    status_event = VisitEventSerializer(write_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = '__all__'

    # def get_status_event(self, obj):
    #     visit_status = VisitEvent.objects.get_or_create(user_id=Type.objects.get(type_name='image'), event_id=obj)
    #     if media.exists():
    #         return media.values_list('url', flat=True)
    #     return None


class EventListSerializer(serializers.ModelSerializer):
    event_image = serializers.SerializerMethodField()
    event_category = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ('title', 'description', 'date_event',
                  'time_event', 'interval_time', 'place',
                  'event_image', 'event_category')

    def get_event_image(self, obj):
        media = EventMedia.objects.filter(types_id=Type.objects.get(type_name='image'), event_id=obj)
        if media.exists():
            return media.values_list('url', flat=True)
        return None

    def get_event_category(self, obj):
        categories = EventCategory.objects.filter(event_id=obj)
        if categories.exists():
            category_names = categories.values_list('category_id', flat=True)
            return Category.objects.filter(id__in=category_names).values_list('category_name', flat=True)
        return None
