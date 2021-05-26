from rest_framework import generics, urls
from django.contrib.auth import get_user_model
from accounts.serializers import (
    AccountCreateSerializer,
    AccountListSerializer,
    AccountDetailSerializer,
)

User = get_user_model()


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountDetailSerializer
    queryset = User.objects.all()


class AccountCreateView(generics.CreateAPIView):
    serializer_class = AccountCreateSerializer


class AccountListView(generics.ListAPIView):
    serializer_class = AccountListSerializer
    queryset = User.objects.all()
