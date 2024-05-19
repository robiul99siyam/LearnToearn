from django.urls import path
from .views import JoinListView, JoinCreateView

urlpatterns = [
    path('list/', JoinListView.as_view(), name='join_list'),
    path('create/', JoinCreateView.as_view(), name='join_create'),
]
