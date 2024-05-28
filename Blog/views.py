from django.shortcuts import render
from rest_framework import viewsets
from .models import BlogModel, ReviewModel
from .serializers import BlogSerializer, ReviewSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    pagination_class = PageNumberPagination
    page_size = 2
    # permission_classes = [IsAdminUser]


class ReviewView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleReviewView(GenericAPIView, UpdateModelMixin, DestroyModelMixin):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
