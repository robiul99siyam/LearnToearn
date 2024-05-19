from rest_framework import serializers
from .models import JoinModel

class JoinModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinModel
        fields = '__all__'
