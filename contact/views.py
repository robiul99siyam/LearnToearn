from django.shortcuts import render
from rest_framework.views import APIView
from .models import ContactModel
from .serializers import ContactSerializer
from rest_framework.response import Response
# Create your views here.



#####################
# for email send
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

def send_transaction_email(fullname, email, message, date):
    message = render_to_string('email.html', {
        'fullname' : fullname,
        'email' : email,
        'message': message, 
        'date': date
    })
    send_email = EmailMultiAlternatives(f"Contact via user", '', to=['hmnizum1714032@gmail.com'])
    send_email.attach_alternative(message, "text/html")
    send_email.send()

#####################
class ContactView(APIView):
    def post(self, request, format=None):
        serializerdata = ContactSerializer(data=request.data)
        if serializerdata.is_valid():
            # name = serializerdata.validated_data.get('name')
            # email = serializerdata.validated_data.get('email')
            # message = serializerdata.validated_data.get('message')
            serializerdata.save()
            date = serializerdata.instance.date
            name = serializerdata.instance.name
            email = serializerdata.instance.email
            message = serializerdata.instance.message
            send_transaction_email(name, email, message, date)
            print(date)
            return Response({'msg' : 'Successfully create data'})
        return Response(serializerdata.errors)
