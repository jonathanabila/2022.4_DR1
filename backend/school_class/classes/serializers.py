from classes.models import Class
from rest_framework import serializers


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Class
        fields = ["name"]
