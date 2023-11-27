from django.contrib import admin

from apps.applications.models.application import Application
from apps.applications.models.category import ApplicationCategory
from apps.applications.models.period import ApplicationPeriod
from apps.applications.models.category_document_type import ApplicationCategoryDocumentType


class ApplicationCategoryDocumentTypeInline(admin.TabularInline):
    model = ApplicationCategoryDocumentType


class ApplicationCategoryAdmin(admin.ModelAdmin):
    inlines = [
        ApplicationCategoryDocumentTypeInline,
    ]


admin.site.register(Application)
admin.site.register(ApplicationCategory, ApplicationCategoryAdmin)
admin.site.register(ApplicationPeriod)
