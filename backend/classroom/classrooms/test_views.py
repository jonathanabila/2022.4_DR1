import requests_mock
from django.test import TestCase
from fixtures.factories.classroom_models import ClassRoomFactory


class ViewsTests(TestCase):
    def test_create_non_class(self) -> None:
        response = self.client.get("/classrooms/")

        assert response.status_code == 200
        assert len(response.json()) == 0

    def test_assert_class_id(self) -> None:
        classroom = ClassRoomFactory()

        response = self.client.get("/classrooms/")

        assert response.status_code == 200
        assert len(response.json()) == 1

        api_classroom = next(iter(response.json()), None)
        assert api_classroom is not None
        assert api_classroom["class_id"] == classroom.class_id

    def test_create_classroom_success(self) -> None:
        with requests_mock.Mocker() as m:
            m.get("/classes/1", status_code=200)
            response = self.client.post("/classrooms/", data={"class_id": 1})

        assert response.status_code == 201

    def test_create_classroom_failure(self) -> None:
        with requests_mock.Mocker() as m:
            m.get("/classes/1", status_code=404)
            response = self.client.post("/classrooms/", data={"class_id": 1})

        assert response.status_code == 400
