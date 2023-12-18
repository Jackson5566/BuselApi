from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    subject = serializers.CharField()
    email = serializers.CharField()
    content = serializers.CharField()
