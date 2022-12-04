from classrooms.models import ClassRoom
from classrooms.serializers import ClassRoomSerializer
from events import SchoolClassEventHandler
from rest_framework import status, viewsets
from rest_framework.response import Response


class ClassRoomsView(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

    def create(self, request, *args, **kwargs):
        if not SchoolClassEventHandler.get(request.data["class_id"]):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
