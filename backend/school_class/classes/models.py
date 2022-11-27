from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=256, null=False)


class Student(models.Model):
    name = models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=256, unique=True)

    classes = models.ForeignKey(
        "Class", related_name="classes", null=True, on_delete=models.SET_NULL
    )
