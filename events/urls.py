from django.urls import path
from events.views import (
    EventCreateView,
    EventDetailView,
    EventListView,
)


urlpatterns = [
    path('create/', EventCreateView.as_view(), name='event-creation'),
    path('<int:pk>/', EventDetailView.as_view()),
    path('', EventListView.as_view(), name='event-list'),
]
