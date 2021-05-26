from django.contrib import admin
from .models import (
    Event, VisitEvent,
    EventCategory, EventMedia,
    Category, Type, Status,
)

admin.site.register(Event)
admin.site.register(VisitEvent)
admin.site.register(EventCategory)
admin.site.register(EventMedia)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Status)
