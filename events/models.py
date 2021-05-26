from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    """Properties of one event"""
    title = models.CharField(verbose_name='event title', max_length=255)
    description = models.TextField(verbose_name='event description', blank=True, null=True)
    date_event = models.DateField(verbose_name='event date')
    time_event = models.TimeField(verbose_name='event time')
    place = models.CharField(verbose_name='address of an event', max_length=255)
    interval_time = models.DurationField(verbose_name='event interval time', blank=True, null=True)

    def __str__(self):
        return self.title


class Status(models.Model):
    """Different statuses of events attendance"""
    STATUSES = (
        ("not selected", "not selected"),
        ("will visit", "will visit"),
        ("won't visit", "won't visit"),
        ("already visited", "already visited"),
    )
    status_name = models.CharField(
        verbose_name='status name',
        choices=STATUSES,
        default=STATUSES[0][0],
        max_length=255
    )

    def __str__(self):
        return self.status_name


class VisitEvent(models.Model):
    """The event attendance status of a specific user"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)


class Category(models.Model):
    """Different types of event categories"""
    CATEGORIES = (
        ("exhibitions", "exhibitions"),
        ("theater", "theater"),
        ("shows", "shows"),
    )
    category_name = models.CharField(verbose_name='category name', choices=CATEGORIES, max_length=255)

    def __str__(self):
        return self.category_name


class EventCategory(models.Model):
    """Intermediate table between events and categories"""
    event_id = models.ManyToManyField(Event)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class Type(models.Model):
    """Different types of event media files"""
    TYPES = (
        ("image", "image"),
        ("music", "music"),
        ("video", "video"),
    )
    type_name = models.CharField(verbose_name='type name', choices=TYPES, max_length=255)

    def __str__(self):
        return self.type_name


class EventMedia(models.Model):
    """Intermediate table between events and types"""
    event_id = models.ManyToManyField(Event)
    types_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    url = models.FileField(upload_to='event_images/', verbose_name='url of a media file')
