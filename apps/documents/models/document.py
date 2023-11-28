from django.db import models
from apps.documents.models.document_type import DocumentType
from apps.documents.models.document_status import DocumentStatus
from apps.applications.models.status import ApplicationStatus


class Document(models.Model):
    application = models.ForeignKey(
        "applications.Application",
        on_delete=models.CASCADE,
        null=True,
        related_name="documents",
    )
    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.CASCADE,
    )

    uploaded_document = models.FileField(
        upload_to="documents",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=DocumentStatus.choices,
        default=DocumentStatus.NOT_CHECKED
    )

    comment = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ("id",)

    @classmethod
    def create_files(cls, documents, application):
        for id_, document in documents.items():
            Document.objects.create(
                application=application,
                uploaded_document=document,
                document_type=DocumentType.objects.get(id=id_),
            )

    def __str__(self) -> str:
        if self.application:
            return str(f"Document: {self.id} - {self.application.applicant}")

        return f"Document: {self.id} / status: {self.status}"

    def save(self, *args, **kwargs) -> None:
        if self.status == DocumentStatus.NEED_CORRECTION:
            self.application.status = ApplicationStatus.NEED_CORRECTION
            self.application.save()

        return super().save(*args, **kwargs)
