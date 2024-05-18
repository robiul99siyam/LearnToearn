from django.shortcuts import render
from rest_framework.views import APIView
from .models import ContactModel
from .serializers import ContactSerializer
from rest_framework.response import Response
# Create your views here.
class ContactView(APIView):
    def post(self, request, format=None):
        serializerdata = ContactSerializer(data=request.data)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response({'msg' : 'Successfully create data'})
        return Response(serializerdata.errors)
