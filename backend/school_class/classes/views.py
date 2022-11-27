from classes.models import Class
from classes.serializers import ClassSerializer
from rest_framework import viewsets


class ClassesView(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
