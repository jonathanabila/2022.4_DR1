from classes.models import Class
from rest_framework import serializers


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Class
        fields = ["id", "name"]
