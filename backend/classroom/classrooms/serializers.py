from classrooms.models import ClassRoom
from rest_framework import serializers


class ClassRoomSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = ClassRoom
        fields = ["id", "created_at", "class_id"]
