from django.db import models
from apps.documents.models.document_type import DocumentType
from apps.applications.models.period import ApplicationPeriod


class ApplicationCategory(models.Model):
    title = models.CharField(max_length=255)
    document_types = models.ManyToManyField(
        DocumentType, through="ApplicationCategoryDocumentType"
    )
    period = models.ForeignKey(
        ApplicationPeriod,
        on_delete=models.DO_NOTHING,
        null=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Application Category"
        verbose_name_plural = "Application Categories"
