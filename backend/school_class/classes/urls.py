from django.urls import path

from . import views

app_name = "classes"

urlpatterns = [
    path("", views.ClassesView.as_view(), name="classes"),
    path("<int:pk>", views.ClassDetailView.as_view(), name="classes-detail"),
]
