from rest_framework import generics
from rest_framework.response import Response
from apps.applications.serializers import ApplicationCategorySerializer
from apps.applications.models.category import ApplicationCategory
from apps.applications.serializers import ApplicationCategoryDocumentTypeSerializer
from apps.applications.models.category_document_type import ApplicationCategoryDocumentType


class ApplicationCategoryListAPIView(generics.ListAPIView):
    serializer_class = ApplicationCategorySerializer
    queryset = ApplicationCategory.objects.all()


class ApplicationCategoryDocumentTypeListAPIView(generics.GenericAPIView):
    serializer_class = ApplicationCategoryDocumentTypeSerializer

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = self.serializer_class(qs, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        app_category_id = self.kwargs["pk"]
        application_category = generics.get_object_or_404(
            ApplicationCategory, id=app_category_id
        )
        document_types = ApplicationCategoryDocumentType.objects.filter(
            application_category=application_category
        ).select_related("document_type")

        return document_types
