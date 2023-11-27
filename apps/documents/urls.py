from django.urls import path

from apps.documents import views

urlpatterns = [
    path(
        "update-status/<int:pk>/",
        views.FileStatusUpdateAPIView.as_view(),
        name="file_status_update",
    ),
    path(
        "update-uploaded-file/<int:pk>/",
        views.UploadedFileUpdateAPIView.as_view(),
        name="uploaded_file_update",
    ),
    path(
        "types/create/",
        views.DocumentTypeCreateAPIView.as_view(),
        name="create_document_type",
    ),
    path(
        "types/update/<int:pk>/",
        views.DocumentTypeUpdateAPIView.as_view(),
        name="update_document_type",
    ),
]
