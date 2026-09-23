from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_students, name="get_students"),
    path("create/", views.create_student, name="create_student"),
    path("<int:student_id>/", views.get_student, name="get_student"),
    path("<int:student_id>/update/", views.update_student, name="update_student"),
    path("<int:student_id>/delete/", views.delete_student, name="delete_student"),
]