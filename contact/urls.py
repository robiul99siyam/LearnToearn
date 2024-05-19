from django.urls import path
from .views import ContactView

urlpatterns = [
    path('create/', ContactView.as_view(), name='contact_create'),
]
