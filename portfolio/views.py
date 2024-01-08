from .serializers import ContactSerializer, WorkSerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from .models import Contact, Work
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.conf import settings
# Create your views here.

class CreateWorkView(APIView):
    permission_classes = (IsAdminUser,)
    def post(self, request, *args,**kwargs):
        values = request.data.get("title", None)
        title= values['title']
        description= values['description']
        image= values['image']
        Work(
            title=title,
            description=description,
            image=image)
        work.save()
        return Response({"message":"Work created successfully"},status=HTTP_200_OK)

class EditWorkView(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        work = Work.objects.get(slug=slug)

        # Get new values from request data
        title = request.data.get('title', work.title)
        description = request.data.get('description', work.description)
        image = request.data.get('image', work.image)

        # Update fields only if new values are different
        if work.title != title:
            work.title = title
        if work.description != description:
            work.description = description
        if work.image != image:
            work.image = image
        work.save()
        return Response({"message": "Work updated successfully"}, status=HTTP_200_OK)
class ContactMeView(ListAPIView):
    permission_classes=(AllowAny,)
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.all().order_by("-date")


class ContactView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer

    def post(self,request,*args,**kwargs):
        values = request.data.get("data", None)

        name= values['name']
        email= values['email']
        message= values['message']

        contact = Contact(
            name=name,
            email=email,
            message=message)
        context ={
            "name": name,
            "email": email,
            "message": message
        }
        send_to_ruth = render_to_string('received.html', context)
        sent_to_contact = render_to_string('sent.html', context)
        message = EmailMessage( 'We have a new contact mail', send_to_ruth, "contact@ruthikegah.com", ["contact@ruthikegah.com"])
        message_receiver = EmailMessage( 'Thank you for contacting me', sent_to_contact, "contact@ruthikegah.com", [email])
        message.content_subtype = 'html'
        message_receiver.content_subtype = 'html'
        message_receiver.send()

        message.send()
        contact.save()
        return Response({"message":"Message sent successfully"},status=HTTP_200_OK)

class WorkView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = WorkSerializer
    queryset = Work.objects.all().order_by("-date")


    def get_queryset(self):
            return Work.objects.all().order_by("-date")


class HomeWorkView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = WorkSerializer
    queryset = Work.objects.all().order_by("-date")[:4]

    def get_queryset(self):
        return Work.objects.all().order_by("-date")[:4]


class WorkDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = WorkSerializer
    queryset = Work.objects.all()

    lookup_field ="slug"
