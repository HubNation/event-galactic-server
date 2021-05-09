from django.urls import path
from . import views


urlpatterns = [
    path('', views.account_registration, name='account-registration'),
]
