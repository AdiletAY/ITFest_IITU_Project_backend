from rest_framework import serializers
from apps.documents.models.document import Document
from apps.documents.models.document_type import DocumentType


class UploadedDocumentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ("uploaded_document",)


class DocumentStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            "status",
            "comment",
        )


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    document_type = DocumentTypeSerializer()

    class Meta:
        model = Document
        fields = "__all__"
