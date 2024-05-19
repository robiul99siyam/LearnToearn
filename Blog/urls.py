from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
# create router object
router = DefaultRouter()
# Register
router.register('blog', views.BlogViewSet, basename='blog')


urlpatterns = [
    path('', include(router.urls)),

    path('review/', views.ReviewView.as_view(), name="reviews"),
    path('review/<int:pk>', views.SingleReviewView.as_view(), name="review"),

]
