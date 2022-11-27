from classrooms.models import ClassRoom
from classrooms.serializers import ClassRoomSerializer
from rest_framework import viewsets


class ClassRoomsView(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
