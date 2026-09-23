from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_profiles, name="get_profiles"),
    path("create/", views.create_profile, name="create_profile"),
    path("<int:student_id>/", views.get_profile, name="get_profile"),
    path("<int:student_id>/update/", views.update_profile, name="update_profile"),
    path("<int:student_id>/delete/", views.delete_profile, name="delete_profile"),
]