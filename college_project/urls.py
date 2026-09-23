from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # API endpoints
    path("students/", include("students.urls")),

    path(
        "student-profile/",
        include("student_profile.urls")
    ),

    path(
        "courses/",
        include("course.urls")
    ),

    # API documentation
    path(
        "schema/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),

    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui"
    ),
]