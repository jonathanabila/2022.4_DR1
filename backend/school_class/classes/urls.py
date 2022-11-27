from django.urls import path

from . import views

app_name = "classes"

urlpatterns = [
    path(
        "", views.ClassesView.as_view({"get": "list", "post": "create"}), name="classes"
    ),
    path(
        "<int:pk>",
        views.ClassesView.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="classes-detail",
    ),
]
