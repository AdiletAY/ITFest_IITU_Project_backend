from django.db import models
from apps.applications.models.category import ApplicationCategory
from apps.documents.models.document_type import DocumentType


class ApplicationCategoryDocumentType(models.Model):
    application_category = models.ForeignKey(
        ApplicationCategory,
        verbose_name="Application Category",
        on_delete=models.CASCADE,
    )
    document_type = models.ForeignKey(
        DocumentType,
        related_name="application_category",
        verbose_name="Related File Type",
        on_delete=models.CASCADE,
    )
    is_necessary = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.application_category.title} <-> {self.document_type.title}"

    class Meta:
        unique_together = ("application_category", "document_type")
        verbose_name = "Document Type"
        verbose_name_plural = "Document Types"
