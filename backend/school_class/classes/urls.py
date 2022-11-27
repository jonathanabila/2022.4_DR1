from django.urls import path

from . import views

app_name = "classes"

urlpatterns = [
    path("", views.ClassesView.as_view({"get": "list"}), name="classes"),
    path("<int:pk>", views.ClassDetail.as_view(), name="classes-detail"),
]
