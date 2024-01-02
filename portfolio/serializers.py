from rest_framework import serializers
from .models import Contact,Work


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"



class WorkSerializer(serializers.ModelSerializer):
    class Meta:

        model = Work
        fields = "__all__"
