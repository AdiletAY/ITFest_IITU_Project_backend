from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("user/", include("apps.users.urls")),
    path("auth/", include("apps.authentication.urls")),
    path("documents/", include("apps.documents.urls")),
    path("applications/", include("apps.applications.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
