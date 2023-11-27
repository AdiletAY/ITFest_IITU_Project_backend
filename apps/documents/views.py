from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.utils.permissions import IsApplicant

from apps.utils.services import send_email
from apps.documents.models.document_type import DocumentType
from apps.documents.models.document_status import DocumentStatus
from apps.documents.models.document import Document
from apps.documents.serializer import (
    DocumentTypeSerializer,
    DocumentStatusUpdateSerializer,
    UploadedDocumentUpdateSerializer,
)


class DocumentTypeCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DocumentTypeSerializer


class DocumentTypeUpdateAPIView(generics.UpdateAPIView):
    queryset = DocumentType.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = DocumentTypeSerializer
    lookup_field = "pk"
    http_method_names = ["patch"]


class DocumentStatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DocumentStatusUpdateSerializer
    http_method_names = ["patch"]
    queryset = Document.objects.all()
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save()
        document = self.get_object()
        email = document.application.applicant.email
        if email and document.status == DocumentStatus.NEED_CORRECTION:
            send_email(
                to_email=email,
                context={"document": document},
                html_template_path="email/document_update.html",
                subject="Academic mobility. Document Status Update",
                message="Document Status was updated",
            )


class UploadedFileUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsApplicant]
    queryset = Document.objects.all()
    serializer_class = UploadedDocumentUpdateSerializer
    lookup_field = "pk"
    http_method_names = ["patch"]

    def check_object_permissions(self, request, obj):
        return super().check_object_permissions(request, obj.application)
