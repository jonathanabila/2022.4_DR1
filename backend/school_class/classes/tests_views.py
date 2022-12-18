from django.test import TestCase


class ViewsTests(TestCase):
    def test_create_non_class(self) -> None:
        response = self.client.get("/classes/")

        assert response.status_code == 200
        assert len(response.json()) == 0

    def test_create(self) -> None:
        response = self.client.post("/classes/", data={"name": "class-name"})

        assert response.status_code == 201
