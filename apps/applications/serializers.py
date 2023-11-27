from apps.users.serializers import UserSerializer
from apps.applications.models.application import Application
from rest_framework import serializers

from apps.applications.models.category_document_type import ApplicationCategoryDocumentType
from apps.applications.models.category import ApplicationCategory
from apps.documents.serializer import DocumentSerializer


class ApplicationCategoryDocumentTypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="document_type.id")
    title = serializers.CharField(source="document_type.title")

    class Meta:
        model = ApplicationCategoryDocumentType
        fields = (
            "id",
            "title",
            "is_necessary",
        )


class ApplicationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationCategory
        exclude = [
            "document_types",
        ]


class ApplicationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            "status",
            "comment",
        )


class ApplicationCreateSerializer(serializers.Serializer):
    category = serializers.IntegerField()
    files = serializers.ListField(child=serializers.FileField())


class ApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer()
    documents = DocumentSerializer(many=True)

    class Meta:
        model = Application
        fields = "__all__"


class PartialApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer()  # partial
    documents = DocumentSerializer(many=True)
    category = ApplicationCategorySerializer()

    class Meta:
        model = Application
        exclude = [
            "comment",
        ]


class UserApplicationSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True)
    category = ApplicationCategorySerializer()

    class Meta:
        model = Application
        exclude = [
            "applicant",
        ]
