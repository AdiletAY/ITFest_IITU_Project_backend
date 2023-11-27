from django.urls import path

from apps.applications.views import application as app_views

urlpatterns = [
    path("", app_views.ApplicationListAPIView.as_view(), name="application_list"),
    path(
        "create/",
        app_views.ApplicationCreateAPIView.as_view(),
        name="application_create",
    ),
    path(
        "detail/<int:pk>/",
        app_views.ApplicationDetailAPIView.as_view(),
        name="application_detail",
    ),
    path(
        "delete/<int:pk>/",
        app_views.ApplicationDeleteAPIView.as_view(),
        name="application_delete",
    ),
    path(
        "update/<int:pk>/",
        app_views.ApplicationUpdateAPIView.as_view(),
        name="application_update",
    ),
    path(
        "my/",
        app_views.UserApplicationListAPIView.as_view(),
        name="user_application_list",
    )
]
