from django.contrib import admin
from apps.documents.models.document import Document
from apps.documents.models.document_type import DocumentType


admin.site.register(Document)
admin.site.register(DocumentType)
