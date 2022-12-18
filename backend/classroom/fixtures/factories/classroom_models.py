import factory.django
from classrooms.models import ClassRoom


class ClassRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClassRoom

    created_at = factory.Faker("date_object")
    class_id = factory.Faker("pyint", min_value=0, max_value=1000)
