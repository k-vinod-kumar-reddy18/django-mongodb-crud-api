from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    # Django Admin
    path(
        "admin/",
        admin.site.urls
    ),

    # Students APIs
    path(
        "students/",
        include("students.urls")
    ),

    # Student Profile APIs
    path(
        "student-profile/",
        include("student_profile.urls")
    ),

    # Course APIs
    path(
        "courses/",
        include("course.urls")
    ),

    # JWT Login
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),

    # JWT Refresh Token
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),

    # OpenAPI Schema
    path(
        "schema/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),

    # Swagger Documentation
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui"
    ),
]