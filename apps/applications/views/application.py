from apps.applications.models.status import ApplicationStatus
from datetime import datetime

from django.db.models import Case, When, Value
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework import generics, parsers, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.documents.models.document import Document
from apps.utils.exceptions import NotAllowed
from apps.utils.permissions import IsApplicantOrAdmin

from apps.utils.services import send_email
from apps.applications.serializers import (
    ApplicationCreateSerializer,
    ApplicationSerializer,
    ApplicationUpdateSerializer,
    PartialApplicationSerializer,
    UserApplicationSerializer,
)
from apps.applications.models.application import ApplicationCategory
from apps.applications.models.category_document_type import ApplicationCategoryDocumentType
from apps.applications.models.application import Application
from apps.documents.models.document import Document


class ApplicationCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ApplicationSerializer
    parser_classes = [parsers.MultiPartParser]

    @extend_schema(request=ApplicationCreateSerializer, responses=ApplicationSerializer)
    def post(self, request, format=None):
        """
        FormData should be in format:
        {
            "category": APPLICATION_CATEGORY_ID,
            "documents": [
                DOCUMENT_TYPE_ID: UPLOADED_FILE,
            ]
        }
        """

        applicant = request.user
        category_id = request.data.get("category")
        category = ApplicationCategory.objects.get(id=category_id)

        if not category:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"detail": f"ApplicationCategory with id {category_id} not found"},
            )

        period = category.period
        if not period.has_valid_duration():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "detail": "The application period is passed"
                },
            )

        files = request.FILES

        document_types = ApplicationCategoryDocumentType.objects.filter(
            application_category=category,
            is_necessary=True,
        )

        uploaded_files_ids = files.keys()
        document_types_in_db = ApplicationCategoryDocumentType.objects.filter(
            application_category=category,
            document_type__id__in=uploaded_files_ids,
            is_necessary=True,
        )

        if document_types_in_db.count() < document_types.count():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "detail": "You should upload all necessary files for this category"
                },
            )

        return self.create_application(applicant, category, files)

    def create_application(self, applicant, category, files):
        is_allowed_to_apply = self.request.user.is_allowed_to_apply()

        if is_allowed_to_apply:
            application = Application.objects.create(
                applicant=applicant,
                category=category,
                course_number=applicant.course_number,
                gpa=applicant.gpa,
            )
            Document.create_files(files=files, application=application)
            return Response(status=status.HTTP_201_CREATED)

        raise NotAllowed


class ApplicationDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsApplicantOrAdmin]
    queryset = (
        Application.objects.all()
        .select_related("applicant")
        .prefetch_related("documents")
    )
    serializer_class = ApplicationSerializer
    lookup_field = "pk"


class UserApplicationListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserApplicationSerializer

    def get_queryset(self):
        applicant = self.request.user
        queryset = (
            Application.objects.filter(applicant=applicant)
            .select_related("category")
            .prefetch_related("documents")
        )
        return queryset


class ApplicationDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsApplicantOrAdmin]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    lookup_field = "pk"


class ApplicationListAPIView(generics.ListAPIView):
    queryset = (
        Application.objects.all()
        .select_related("applicant")
        .prefetch_related("documents")
        .order_by(Case(
            When(status=ApplicationStatus.SENT, then=Value(0)),
            When(status=ApplicationStatus.NEED_CORRECTION, then=Value(1)),
            When(status=ApplicationStatus.REJECTED, then=Value(3)),
            default=Value(2),
        ), "sent_date")
    )
    serializer_class = PartialApplicationSerializer
    pagination_class = PageNumberPagination
    page_size = 1
    permission_classes = [IsAdminUser]


class ApplicationUpdateAPIView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    http_method_names = ["patch"]
    serializer_class = ApplicationUpdateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "pk"

    def perform_update(self, serializer):
        application = serializer.save(check_date=timezone.now())

        email = application.applicant.email

        statuses = (
            ApplicationStatus.REJECTED,
            ApplicationStatus.APPROVED,
        )

        if email and application.status in statuses:
            send_email(
                to_email=email,
                context={"application": application},
                html_template_path="email/application_update.html",
                subject="Academic Mobility. Status Update",
                message="Application Status Update",
            )

        return serializer.data
