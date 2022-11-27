from django.urls import path

from . import views

app_name = "classrooms"

urlpatterns = [
    path(
        "",
        views.ClassRoomsView.as_view({"get": "list", "post": "create"}),
        name="classrooms",
    ),
    path(
        "<int:pk>",
        views.ClassRoomsView.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="classroom-detail",
    ),
]
