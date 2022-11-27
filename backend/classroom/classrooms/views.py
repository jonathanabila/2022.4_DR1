from classrooms.models import ClassRoom
from classrooms.serializers import ClassRoomSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response

# TODO: Identify why this is isn't importing from the library.
from libs.events.events.events import SchoolClassEventHandler  # type: ignore


class ClassRoomsView(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

    def create(self, request, *args, **kwargs):
        if not SchoolClassEventHandler.get(request.data["class_id"]):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
