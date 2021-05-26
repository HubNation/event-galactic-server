from django.urls import path
from accounts.views import (
    AccountCreateView,
    AccountListView,
    AccountDetailView,
)


urlpatterns = [
    path('register/', AccountCreateView.as_view(), name='user-register'),
    path('profiles/', AccountListView.as_view(), name='user-profiles'),
    path('profiles/<int:pk>/', AccountDetailView.as_view()),
]
