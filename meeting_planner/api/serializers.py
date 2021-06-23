from django.db.models import fields
from rest_framework import serializers

from meetings.models import Room, Meeting


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'
