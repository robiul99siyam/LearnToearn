from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import JoinModel
from .serializers import JoinModelSerializer
from django.utils.timezone import datetime

class JoinListView(generics.ListAPIView):
    queryset = JoinModel.objects.all()
    serializer_class = JoinModelSerializer
    permission_classes = [IsAdminUser]

class JoinCreateView(generics.CreateAPIView):
    queryset = JoinModel.objects.all()
    serializer_class = JoinModelSerializer


