import enum

from django.db import models
from django.utils import timezone


class StudentClassRoomStatus(enum.Enum):
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    LATE = "LATE"
    SICK = "SICK"
    OTHER = "OTHER"


class ClassRoom(models.Model):
    created_at = models.DateField(default=timezone.now)
    class_id = models.IntegerField(null=False)


class Attendence(models.Model):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    student_id = models.IntegerField(null=False)

    status = models.CharField(
        choices=[(e.value, e.name) for e in StudentClassRoomStatus], max_length=256
    )
